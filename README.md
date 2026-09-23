# cishu

## 辞书、词汇语义与RAG：课程文献综述写作包

**建议题目：辞书知识与检索增强生成的融合：语义表示、技术路径与发展趋势。**

用于《专业写作基础》课程，写作包版本v0.2，检索截止2026-09-22。主线是“辞书为什么与语义计算及RAG结合、怎样结合、已有证据的边界及未来方向”，不是个人研究项目开题报告。

| 文件 | 内容 |
|---|---|
| [01_references.md](01_references.md) | 35项主参考文献，逐项给出原始入口、写作用途、限制和本轮访问深度；另有1项中文拓展书目 |
| [02_outline.md](02_outline.md) | 标题、中心论点、概念边界、逐节论证安排、字数建议及提交检查 |
| [03_draft.md](03_draft.md) | 完整中文综述初稿，已由维护者上传；正文及35项引文保持原样 |
| [04_search_and_evidence.md](04_search_and_evidence.md) | 检索范围、纳入标准、证据分类、版本核验和全文访问限制 |
| [slides/cishu_literature_review.pptx](slides/cishu_literature_review.pptx) | 27页可编辑课堂汇报PPT，正文23页＋参考文献附录4页 |
| [slides/cishu_literature_review.pdf](slides/cishu_literature_review.pdf) | 与PPT对应的PDF预览 |
| [slides/speaker_notes.md](slides/speaker_notes.md) | 逐页讲稿、建议用时、初稿章节与参考文献对应 |
| [slides/README.md](slides/README.md) | 演示文稿使用与重建说明 |
| [CHANGELOG.md](CHANGELOG.md) | 写作包更新记录 |

## 使用顺序

先看大纲确认课程选题，再依据参考清单核读重点原文，最后修改初稿。初稿主体约7800个汉字（不含参考文献；不是Word词数），使用统一的[1]—[35]引文编号。文本材料使用UTF-8 Markdown，可在GitHub直接阅读。课堂汇报可使用配套PPT及逐页讲稿；PPT建议约17—20分钟，参考附录按需展示。PDF用于快速预览。

## 写作原则

- 区分模型辅助辞书编纂与辞书增强模型回答。
- 以辞书和语义问题为中心，不堆砌通用RAG模型名称。
- 区分直接辞书RAG证据、相邻技术证据与本文提出的未来建议。
- 不把预印本写成正式发表论文，不把社区规范写成W3C标准。
- 本包不包含作者自造的实验数据或性能结果；全部内容限定为课程文献综述。

## 提交前

本包是AI辅助检索与写作初稿，不等于已经完成的独立学术论文。请按课程政策核读、修改并说明辅助方式；作者、学号、课程格式等由本人填写。部分论文本轮只核验元数据和摘要，访问深度逐项列出。未登录知网或万方作穷尽检索，因此不声称系统覆盖所有中文研究。

公开仓库当前包含参考信息、大纲、初稿、课堂演示及工作记录，不收录商业辞书全文或受限论文附件。

## 演示文稿更新

PPT根据仓库初稿制作，保留原有引文编号及证据边界，不新增研究结果。讲稿已同时写入PowerPoint备注页。字体为Noto Sans CJK SC／Noto Serif CJK SC，字体未随仓库分发；缺少字体时可使用PDF预览。

编辑 `slides/presentation.json` 后，可运行 `python scripts/build_presentation.py --pdf` 重建。自动构建只更新演示成品，不覆盖初稿、文献清单或README；完整说明见 `slides/README.md`。
