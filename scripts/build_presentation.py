#!/usr/bin/env python3
"""Build an editable course deck and accompanying notes from reviewed slide data.
Python 3.10+, python-pptx==1.0.2. No network calls or model API calls.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt

ROOT=Path(__file__).resolve().parents[1]
W,H=13.333333,7.5
FONT='Noto Sans CJK SC'
SERIF='Noto Serif CJK SC'
C={'bg':'F6F7F3','ink':'14353C','body':'344C52','mute':'65777A','teal':'176B62','gold':'B07A3F','line':'D5E1DB','white':'FFFFFF','pale':'E7F0EB','dark':'102F36'}
GEOMETRY=[]

def rgb(v): return RGBColor.from_string(C.get(v,v))
def box(slide,x,y,w,h,fill='white',line=None,kind=MSO_SHAPE.RECTANGLE):
    s=slide.shapes.add_shape(kind,Inches(x),Inches(y),Inches(w),Inches(h))
    s.fill.solid();s.fill.fore_color.rgb=rgb(fill)
    if line: s.line.color.rgb=rgb(line);s.line.width=Pt(.7)
    else:s.line.fill.background()
    return s

def text(slide,content,x,y,w,h,size=20,color='body',bold=False,font=FONT,align=PP_ALIGN.LEFT):
    s=slide.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    tf=s.text_frame;tf.clear();tf.word_wrap=True
    tf.margin_left=0;tf.margin_right=0;tf.margin_top=0;tf.margin_bottom=0
    for j,line in enumerate(str(content).split('\n')):
        p=tf.paragraphs[0] if j==0 else tf.add_paragraph()
        p.alignment=align;p.space_before=Pt(0);p.space_after=Pt(size*.20);p.line_spacing=1.15
        r=p.add_run();r.text=line;r.font.name=font;r.font.size=Pt(size);r.font.bold=bold;r.font.color.rgb=rgb(color)
        rp=r._r.get_or_add_rPr();ea=OxmlElement('a:ea');ea.set('typeface',font);rp.append(ea)
    GEOMETRY.append({'slide':len(slide.part.package.presentation_part.presentation.slides),'text':str(content),'x':x,'y':y,'w':w,'h':h,'font_size':size})
    return s

def line(slide,x1,y1,x2,y2,color='line',width=1.2):
    s=slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y1),Inches(x2),Inches(y2))
    s.line.color.rgb=rgb(color);s.line.width=Pt(width)
    return s

def banner(slide,value,dark=False):
    if not value:return
    box(slide,.62,6.24,12.09,.58,'teal' if not dark else 'pale')
    text(slide,value,.83,6.35,11.65,.34,15,'white' if not dark else 'ink',True)

def chrome(prs,meta,index,total):
    slide=prs.slides.add_slide(prs.slide_layouts[6]);slide.background.fill.solid();slide.background.fill.fore_color.rgb=rgb('bg')
    box(slide,0,0,W,.07,'teal')
    text(slide,'专业写作基础  /  文献综述汇报',.62,.27,7,.25,10.5,'teal',True)
    text(slide,meta.get('tag',''),9.3,.27,3.4,.25,10.5,'mute',False,align=PP_ALIGN.RIGHT)
    text(slide,meta['title'],.62,.8,12.0,.65,29,'ink',True)
    text(slide,meta.get('subtitle',''),.64,1.54,11.97,.55,14,'mute')
    banner(slide,meta.get('takeaway',''))
    line(slide,.62,7.05,12.7,7.05,'line',.7)
    refs=' '.join('['+str(n)+']' for n in meta.get('refs',[]))
    text(slide,('依据：初稿 '+meta.get('section','')+'  '+refs).strip(),.65,7.15,10.75,.2,9,'mute')
    text(slide,f'{index:02d} / {total:02d}',11.9,7.12,.8,.25,10,'mute',align=PP_ALIGN.RIGHT)
    return slide

def cards(slide,items,y=2.35,h=3.52,cols=None):
    n=cols or len(items);gap=.23;cw=(12.08-gap*(n-1))/n
    for i,item in enumerate(items):
        x=.63+i*(cw+gap);box(slide,x,y,cw,h,'white','line');box(slide,x,y,cw,.055,'teal')
        text(slide,f'{i+1:02d}',x+.23,y+.22,.6,.5,23,'gold',True)
        text(slide,item[0],x+.23,y+.94,cw-.46,.75,22 if n<4 else 19,'ink',True)
        text(slide,item[1],x+.23,y+1.78,cw-.46,h-1.9,18 if n<4 else 16.5,'body')

def render(prs,m,i,total):
    s=chrome(prs,m,i,total);items=m['items'];kind=m['kind']
    if kind=='cover':
        s.background.fill.fore_color.rgb=rgb('dark')
        # Replace the generic header with cover artwork and title; all shapes remain editable.
        for shape in list(s.shapes):
            el=shape._element;el.getparent().remove(el)
        text(s,'专业写作基础  ·  文献综述汇报',.75,.7,8,.4,14,'A8CEBF',True)
        text(s,'辞书知识与\n检索增强生成的融合',.75,1.65,9.2,1.95,38,'white',True,font=SERIF)
        text(s,m['subtitle'],.8,4.0,8.3,.5,21,'D6E7E0')
        line(s,.8,4.82,7.2,4.82,'gold',2)
        text(s,'从词条查询走向可追溯的语言知识服务',.8,5.18,8.3,.5,19,'white')
        text(s,'2026年9月  |  文献范围沿用初稿：截至2026-09-22',.8,6.5,9,.3,11,'AAC0BD')
        for j,(label,x,y) in enumerate([('辞书',10.3,1.3),('语义',9.45,3.35),('证据',11.18,3.35),('生成',10.3,5.25)]):
            if j:line(s,10.92,1.95,x+.58,y+.55,'406770',1.5)
            box(s,x,y,1.22,1.12,'1B4650',kind=MSO_SHAPE.OVAL)
            text(s,label,x+.1,y+.38,1.02,.36,18,'white',True,align=PP_ALIGN.CENTER)
        return s
    if kind in {'questions','cards','case'}:
        cards(s,items)
    elif kind=='evidence':
        for j,item in enumerate(items):
            y=2.22+j*1.19;box(s,.64,y,12.05,1.03,'white','line')
            box(s,.64,y,2.2,1.03,'teal' if j==2 else 'pale')
            text(s,item[0],.88,y+.32,1.8,.4,21,'white' if j==2 else 'teal',True)
            text(s,item[1],3.08,y+.22,6.25,.6,18,'body')
            text(s,item[2],9.5,y+.28,2.9,.45,16,'gold',True)
    elif kind=='timeline':
        xs=[.65,3.75,6.85,9.95];line(s,.92,3.02,12.45,3.02,'teal',2)
        for j,(year,label,body) in enumerate(items):
            x=xs[j];text(s,year,x,2.36,2.8,.42,22,'teal',True)
            box(s,x+.05,2.92,.2,.2,'gold',kind=MSO_SHAPE.OVAL)
            text(s,label,x,3.45,2.7,.66,21,'ink',True)
            text(s,body,x,4.34,2.77,1.1,18,'body')
    elif kind=='table':
        widths=[3.05,4.08,4.92];y=2.24;rh=3.65/len(items)
        for row,vals in enumerate(items):
            x=.64
            for col,(val,w) in enumerate(zip(vals,widths)):
                box(s,x,y,w-.025,rh-.025,'teal' if row==0 else ('white' if row%2 else 'pale'))
                text(s,val,x+.16,y+.14,w-.34,rh-.16,15.5 if row else 16,'white' if row==0 else ('ink' if col==0 else 'body'),row==0 or col==0)
                x+=w
            y+=rh
    elif kind=='layers':
        for j,(num,name,examples,question) in enumerate(items):
            y=2.25+j*1.19;box(s,.65,y,12.04,1.02,'white','line')
            text(s,num,.88,y+.21,.6,.5,27,'gold',True)
            text(s,name,1.73,y+.22,2.72,.5,20,'ink',True)
            text(s,examples,4.7,y+.25,4.03,.55,17,'teal')
            text(s,question,9.0,y+.24,3.25,.6,17,'body')
    elif kind in {'dual','quality'}:
        for j,item in enumerate(items):
            x=.65+j*6.18;box(s,x,2.28,5.87,3.58,'white','line')
            text(s,item[0],x+.28,2.57,5.28,.53,23,'ink',True)
            line(s,x+.28,3.28,x+5.55,3.28,'gold',1.5)
            text(s,item[1],x+.28,3.56,5.26,1.75,20,'body')
            if len(item)>2:text(s,item[2],x+.28,5.34,5.26,.34,15,'teal',True)
    elif kind=='pipeline':
        for j,(name,body) in enumerate(items):
            x=.65+j*2.46;box(s,x,2.83,2.19,2.14,'teal' if j in (0,4) else 'white','line')
            text(s,str(j+1),x+.18,3.02,.45,.45,22,'gold',True)
            text(s,name,x+.17,3.66,1.85,.46,21,'white' if j in (0,4) else 'ink',True)
            text(s,body,x+.17,4.28,1.85,.66,14.2,'white' if j in (0,4) else 'body')
            if j<4:box(s,x+2.24,3.66,.15,.33,'gold',kind=MSO_SHAPE.CHEVRON)
        text(s,'检索结果需要义项与来源判断；生成结果需要证据回查。',1.3,5.47,10.72,.45,19,'teal',True,align=PP_ALIGN.CENTER)
    elif kind=='evaluation':
        for j,(label,terms,q) in enumerate(items):
            y=2.2+j*.93;box(s,.65,y,12.04,.8,'white' if j%2==0 else 'pale')
            text(s,label,.88,y+.18,1.45,.4,20,'teal',True)
            text(s,terms,2.8,y+.19,4.12,.38,17,'body')
            text(s,q,7.24,y+.19,5.07,.38,17,'ink')
    elif kind=='diagnosis':cards(s,items)
    elif kind=='future':
        for j,(name,body) in enumerate(items):
            x=.65+(j%2)*6.18;y=2.22+(j//2)*1.94
            box(s,x,y,5.86,1.7,'white','line')
            text(s,name,x+.25,y+.24,5.3,.42,22,'teal',True)
            text(s,body,x+.25,y+.85,5.27,.7,18,'body')
    elif kind=='closing':
        for j,(name,body) in enumerate(items):
            y=2.4+j*1.12;text(s,name,.78,y,1.65,.53,25,'teal',True)
            text(s,body,2.58,y+.05,9.72,.7,22,'ink')
    else:raise ValueError('Unknown slide layout '+kind)
    return s


def bib(prs,refs,start,end,idx,total):
    m={'title':f'参考文献（{(start-1)//9+1}/4）','subtitle':'编号与初稿一致；原始链接可点击。完整卷期、页码及阅读深度见文献清单。','section':'参考文献','tag':'参考附录','refs':[],'takeaway':''}
    s=chrome(prs,m,idx,total)
    for j,n in enumerate(range(start,end+1)):
        raw=refs[n];before=raw.split(' [原始来源]')[0]
        # Keep citation wording; exclude journal details only when the entry is too long for projection.
        match=re.match(r'(.+?\[(?:J|C|EB/OL|R/OL)\])\.',before)
        shown=match.group(1) if match else before
        years=re.findall(r'\b(?:19|20)\d{2}\b',before);year=years[-1] if years else ''
        y=2.15+j*.525
        text(s,f'[{n}]',.67,y,.5,.4,13,'teal',True)
        tb=text(s,shown+'  '+year,1.26,y,11.33,.5,12.3,'body')
        url=re.search(r'\[原始来源\]\((https?://[^)]+)\)',raw).group(1)
        for p in tb.text_frame.paragraphs:
            for r in p.runs:r.hyperlink.address=url
        line(s,.67,y+.495,12.68,y+.495,'line',.55)
    return s


def deterministic_zip(path):
    raw=path.read_bytes();out=io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(raw)) as zin, zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as zout:
        for name in sorted(zin.namelist()):
            item=zipfile.ZipInfo(name,(2026,9,23,0,0,0));item.compress_type=zipfile.ZIP_DEFLATED;item.external_attr=0o600<<16
            zout.writestr(item,zin.read(name))
    path.write_bytes(out.getvalue())


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pdf',action='store_true');args=ap.parse_args()
    data=json.loads((ROOT/'slides/presentation.json').read_text(encoding='utf-8'))
    draft=(ROOT/'03_draft.md').read_bytes()
    if hashlib.sha256(draft).hexdigest()!=data['source_draft_sha256']:
        raise SystemExit('Draft changed: review slide wording and update the recorded source hash before rebuilding.')
    refs={int(n):v for n,v in re.findall(r'^\[(\d+)\] (.+)$',draft.decode('utf8'),re.M)}
    if set(refs)!=set(range(1,36)):raise ValueError('Expected the 35 reference IDs used by this reviewed deck.')
    prs=Presentation();prs.slide_width=Inches(W);prs.slide_height=Inches(H)
    props=prs.core_properties;props.title=data['title'];props.subject='专业写作基础课程文献综述';props.author='课程文献综述';props.keywords='辞书,词汇语义,RAG,文献综述';props.comments='Based on the repository draft; editable shapes and slide notes.'
    props.created=props.modified=datetime(2026,9,23,tzinfo=timezone.utc)
    slides=data['slides'];total=len(slides)+4;notes=['# 配套PPT逐页讲稿\n',f"正文{len(slides)}页，参考文献附录4页；建议正文约17—20分钟，附录按需展示。\n\n内容依据：`03_draft.md`（来源提交 `{data['source_commit']}`）。文献范围沿用初稿截至{data['literature_cutoff']}的清单；本次未新增外部研究。\n"]
    for i,m in enumerate(slides,1):
        if not set(m['refs'])<=refs.keys():raise ValueError('Missing bibliography ID')
        s=render(prs,m,i,total)
        citations='\n'.join(f'[{n}] {refs[n]}' for n in m['refs'])
        nt=f"第{i}页｜{m['title']}\n对应初稿：{m['section']}\n建议用时：{m['seconds']}秒\n\n{m['notes']}\n\n参考来源（沿用初稿）：\n{citations}"
        s.notes_slide.notes_text_frame.text=nt
        notes.append(f"## {i:02d} {m['title']}\n\n对应初稿：{m['section']}；建议{m['seconds']}秒。\n\n{m['notes']}\n\n{citations}\n")
    for j,start in enumerate([1,10,19,28]):
        end=min(start+8,35);s=bib(prs,refs,start,end,len(slides)+j+1,total)
        s.notes_slide.notes_text_frame.text='参考文献附录；编号、文献身份与初稿一致。\n'+'\n'.join(f'[{n}] {refs[n]}' for n in range(start,end+1))
    output=ROOT/'slides/cishu_literature_review.pptx';prs.save(output);deterministic_zip(output)
    (ROOT/'slides/speaker_notes.md').write_text('\n'.join(notes),encoding='utf8')
    bounds=[]
    for i,s in enumerate(prs.slides,1):
        for sh in s.shapes:
            if sh.left<0 or sh.top<0 or sh.left+sh.width>prs.slide_width+20 or sh.top+sh.height>prs.slide_height+20:
                bounds.append({'slide':i,'shape':sh.name})
    if bounds:raise ValueError('Out-of-slide shape: '+str(bounds))
    if args.pdf:
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(['libreoffice','-env:UserInstallation=file://'+d,'--headless','--convert-to','pdf','--outdir',str(output.parent),str(output)],check=True,timeout=180)
        if not output.with_suffix('.pdf').exists():raise RuntimeError('PDF export was not created.')
    artifact_files=[output,ROOT/'slides/speaker_notes.md']
    if output.with_suffix('.pdf').exists():artifact_files.append(output.with_suffix('.pdf'))
    report={'presentation_version':data['version'],'build_date':data['date'],'source_commit':data['source_commit'],'source_draft_sha256':data['source_draft_sha256'],'main_slides':len(slides),'reference_slides':4,'total_slides':total,'reference_entries':len(refs),'all_slides_have_notes':all(s.has_notes_slide for s in prs.slides),'editable_text_and_shapes':True,'out_of_slide_shapes':bounds,'font':FONT,'source_policy':'Adaptation of the existing draft; no new research or model results.','files':{str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in artifact_files}}
    (ROOT/'slides/build_manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
