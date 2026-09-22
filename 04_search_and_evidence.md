# 文献检索、核验与证据边界记录

## 1. 本轮范围

日期：2026-09-22。用途：《专业写作基础》课程综述准备。主题：辞书知识、词汇语义与检索增强生成的连接。主清单35项，另列1项仅核验书目的中文拓展阅读。

这是有选择的主题式文献综述，不是系统综述或元分析。不报告未经保存和核实的初检数量、排除数量或PRISMA流程。未登录知网、万方、Web of Science或Scopus进行穷尽检索；不能在提交稿中声称已经全面覆盖国内外研究。

## 2. 检索与核验路径

实际采用公开网页搜索定位，再回到论文原站、正式论文集、出版页、社区规范或作者机构记录核验。使用的平台包括ACL Anthology、NeurIPS、ICLR、arXiv、International Journal of Lexicography出版页、EURALEX、W3C及研究机构页面。

下列检索式用于概括本轮主题和供后续重跑，不是逐次搜索引擎请求的原始日志，也不代表结果穷尽：

```text
lexicography electronic dictionary corpus examples
lexicography generative AI ChatGPT
word sense alignment monolingual dictionaries
WordNet FrameNet BabelNet OpenHowNet sememe
TEI Lex-0 OntoLex semantics by reference
definition generation specificity interpretable word sense
reverse dictionary WantWords
retrieval augmented generation dictionary lexicographic knowledge
low resource translation dictionary retrieval Mambai
Doha historical dictionary retrieval augmented generation
IRCoT Self-RAG Adaptive-RAG Think-on-Graph GraphRAG HippoRAG
citation generation ALCE RAGAs evidence evaluation
辞书 大语言模型 例句 质量评估
义原 表示学习 词向量
```

检索范围确定后，对关键论文按准确题名或已知论文ID核验。优先采用正式发表版本；无法确认正式版本的，以明确的预印本版本著录，不自行补造会议、卷期或页码。

## 3. 纳入与排除

纳入：与辞书数字化、词汇语义表示、释义／例句生成、直接辞书检索增强、可迁移的检索机制或评价方法有明确联系，且存在可核验原始入口的材料。

排除或不作为正文证据：来源不明的中文“词典JSON”、只有宣传文案的产品页、无法回到原始论文的二手排行榜、私人项目报告、未验证实验结果以及只有标题关联的通用LLM论文。

中文新书《数字辞书智能化编纂：大语言模型的创新应用》仅核验出版社书目和介绍，列于扩展阅读，不支持正文具体论断。此前私人Core–Range讨论与数据审计不是本综述的公开学术证据，不复制到公开仓库。

## 4. 不同证据类型怎样使用

| 类型 | 本清单中的代表 | 可以支持 | 不可直接支持 |
|---|---|---|---|
| 辞书应用直接证据 | [29] Mambai；[30]多哈历史辞书 | 相应语言、资源和任务中的辞书接入可行性 | 所有中文辞书任务均有同等增益 |
| 语义与辞书基础 | [4] MWSA；[5]WordNet；[8]OpenHowNet；[11]OntoLex | 表示单位、关系、互操作、对齐问题 | RAG性能已提高 |
| 模型内知识融合 | [9]中文义原词向量；[21]SememeLRM | 结构知识在受测训练方案中的作用 | 同一知识直接放prompt效果必然相同 |
| 通用检索方法 | [3]RAG；[22]DPR；[23]—[28] | 检索和控制机制、相邻任务证据 | 已验证的辞书专用系统 |
| 生成与质量评价 | [16]—[20]；[31]—[35] | 具体性、例句质量、证据与评价问题 | 完全取消人工审核 |

上述编号与初稿、参考清单一致。引用某项技术文献之后提出辞书应用建议时，初稿采用“可探索”“本文据此建议”等表达，表明这是综述推论，不是原作者已经报告的辞书实验。

## 5. 关键原文核读位置

- [11] OntoLex-Lemon：Status of This Document；2.1 Purpose；3章词条、词形及语义引用相关内容。确认社区报告身份以及semantics by reference原则。
- [21] SememeLRM：正文STC方法和模型／实验设置相关段落。确认结构义原构建与模型内融合路线，不把词汇关系分类写成RAG问答。
- [23] IRCoT：方法相关段落。确认检索与中间推理交替，不把后续所有适应性RAG都概括为同一训练策略。
- [29] Mambai：第3—4节及实验讨论相关段落。核读词典条目整理、平行句检索、输入构成与任务限制。
- [30] 多哈历史辞书：意图路由、训练设置及结论相关段落。核对混合检索、经训练的重排／分类组件和自动／人工评价的范围。
- [19] CCL2025：原文首页图像核对中文作者和题名；摘要核对五维评价框架以及结果所指对象。
- 其他条目的访问深度在 `01_references.md` 逐项注明。不能将“已找到正式页面”写成“全文已精读”。

## 6. 年份、版本与元数据检查

- [5] WordNet 1995的书目信息由Princeton项目官方引用页核对；出版入口另保留DOI。
- [10] TEI Lex-0为2018机构著录的技术报告／社区建议；在线规范可能继续更新，不能把当前网页所有变化都归到2018。
- [11] OntoLex 2016不是W3C Recommendation。
- [14] Noraset采用AAAI2017正式发表年，而不是早期预印本年。
- [21] SememeLRM采用ACL2026正式页4930—4947。
- [24] Self-RAG采用ICLR2024正式版本。
- [27] GraphRAG初版2024；本清单采用2025-02-19的v2，作者和版本一致。
- [30] 多哈历史辞书RAG采用2026-03-25预印本；本轮未确认另有正式发表版本。
- [32] RAGAs采用EACL2024正式论文；[33] Lost in the Middle采用TACL2024版本。
- [19] CCL2025文中98.6%不是“生成例句全部正确率”；初稿没有引用该数字作质量结论。

## 7. 后续需要补的材料

取得课程的字数、引用格式及AI辅助要求；通过学校图书馆补读中文辞书学研究和重点期刊全文；对本轮只读摘要的重点文献继续记录方法、样本、评价与局限。若课程规定只引同行评审论文，应把预印本和社区规范单独列为技术资料，并调整正文措辞，而非修改其发表身份。

本轮没有下载并再分发整篇论文，没有上传商业辞书原文数据库，没有运行新模型实验，没有制造问卷或人工评价数据。
