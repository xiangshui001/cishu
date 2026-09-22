# 参考文献清单与阅读说明

检索截止：2026-09-22。主清单35项，编号按初稿首次引用顺序统一。该清单同时包括正式论文、预印本及社区技术规范，不能一概称为“35篇同行评审论文”。采用便于课程修改的顺序编码形式，出版项与链接已尽量核对；提交时再按课程指定格式统一会议名称、出版地等细节。

**核验不等于全文精读。**下面逐项标明本轮访问深度和能支持的论点；仅核对摘要或目录的材料不用于细节性实验结论。大部分技术条目来自公开英文论文，已纳入两篇中文CCL研究；未登录知网、万方等数据库进行穷尽检索。

## 优先核读的12项

[1] Lexicographers’ Dreams in the Electronic-Dictionary Age、[2] Generative AI and Lexicography、[3] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks、[4] A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment、[8] OpenHowNet、[11] Lexicon Model for Ontologies、[16] Definition Modelling for Appropriate Specificity、[21] Enhancing Lexical Relation Mining with Structured Sememe Knowledge、[29] Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting、[30] Grounding Arabic LLMs in the Doha Historical Dictionary、[31] Enabling Large Language Models to Generate Text with Citations、[32] RAGAs。

顺序建议：先读电子辞书与词义对齐背景，再读RAG基础与两个直接应用案例，最后读结构表示、生成质量及证据评价。不是先把所有通用RAG论文读完才回到辞书。

## 主清单

### [1] Lexicographers’ Dreams in the Electronic-Dictionary Age

DE SCHRYVER G M. Lexicographers’ Dreams in the Electronic-Dictionary Age[J]. International Journal of Lexicography, 16(2): 143–199, 2003. [原始来源](https://doi.org/10.1093/ijl/16.2.143). DOI: 10.1093/ijl/16.2.143.

**主题／身份：**数字辞书；已发表论文。

**写作用途：**交代电子辞书的检索、媒介和服务变化。 **边界：**讨论技术愿景，不是RAG效果实验。

**本轮访问：**作者机构记录及出版信息与摘要。 [补充核验入口](https://biblio.ugent.be/publication/209391)。

### [2] Generative AI and Lexicography: The Current State of the Art Using ChatGPT

DE SCHRYVER G M. Generative AI and Lexicography: The Current State of the Art Using ChatGPT[J]. International Journal of Lexicography, 36(4): 355–387, 2023. [原始来源](https://doi.org/10.1093/ijl/ecad021). DOI: 10.1093/ijl/ecad021.

**主题／身份：**生成式辞书学；已发表论文。

**写作用途：**说明ChatGPT进入辞书研究后的任务和争论。 **边界：**早期研究与示例的评价不能证明可完全替代编纂者。

**本轮访问：**出版页元数据与摘要。

### [3] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).

**主题／身份：**RAG基础；已发表论文。

**写作用途：**定义参数知识与外部检索知识的结合。 **边界：**原始方法包含训练；不能把RAG定义为一概无需训练。

**本轮访问：**元数据与摘要。 [补充核验入口](https://arxiv.org/abs/2005.11401)。

### [4] A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment

AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).

**主题／身份：**义项对齐；已发表论文。

**写作用途：**讨论跨辞书等价、宽窄、相关关系及多语言数据。 **边界：**15种语言中的单语对齐，不是把不同语言彼此对齐。

**本轮访问：**元数据与摘要。

### [5] WordNet: A Lexical Database for English

MILLER G A. WordNet: A Lexical Database for English[J]. Communications of the ACM, 38(11): 39–41, 1995. [原始来源](https://doi.org/10.1145/219717.219748). DOI: 10.1145/219717.219748.

**主题／身份：**词汇语义资源；已发表论文。

**写作用途：**以synset和词汇语义关系解释结构化语义网络。 **边界：**不是普通辞书的版式模型，也不等于RAG系统。

**本轮访问：**项目官方引用页及资源说明。 [补充核验入口](https://wordnet.princeton.edu/citing-wordnet)。

### [6] The Berkeley FrameNet Project

BAKER C F, FILLMORE C J, LOWE J B. The Berkeley FrameNet Project[C]. 36th Annual Meeting of the ACL and 17th International Conference on Computational Linguistics, Volume 1: 86–90, 1998. [原始来源](https://aclanthology.org/P98-1013/). DOI: 10.3115/980845.980860.

**主题／身份：**框架语义；已发表论文。

**写作用途：**说明框架、参与者及词汇与语料的连接。 **边界：**框架角色不应与词性、义原或义项ID混同。

**本轮访问：**元数据与摘要。

### [7] BabelNet: Building a Very Large Multilingual Semantic Network

NAVIGLI R, PONZETTO S P. BabelNet: Building a Very Large Multilingual Semantic Network[C]. Proceedings of ACL 2010: 216–225, 2010. [原始来源](https://aclanthology.org/P10-1023/).

**主题／身份：**多语言语义网络；已发表论文。

**写作用途：**讨论词汇与百科知识的资源连接。 **边界：**连接扩大覆盖，并不消除不同资源的粒度差异。

**本轮访问：**元数据与摘要。

### [8] OpenHowNet: An Open Sememe-based Lexical Knowledge Base

QI F, YANG C, LIU Z, et al. OpenHowNet: An Open Sememe-based Lexical Knowledge Base[EB/OL]. arXiv:1901.09957, 2019. [原始来源](https://arxiv.org/abs/1901.09957). DOI: 10.48550/arXiv.1901.09957.

**主题／身份：**义原知识；预印本。

**写作用途：**说明HowNet式义原知识及可访问接口。 **边界：**本清单按预印本著录；不凭软件许可证推定其他辞书授权。

**本轮访问：**预印本摘要及官方资源说明。 [补充核验入口](https://openhownet.thunlp.org/about_hownet)。

### [9] 基于义原表示学习的词向量表示方法

于宁, 王江萍, 石宇, 等. 基于义原表示学习的词向量表示方法[C]. 第二十届中国计算语言学大会论文集: 57–65, 2021. [原始来源](https://aclanthology.org/2021.ccl-1.6/).

**主题／身份：**中文义原建模；已发表论文。

**写作用途：**补充中文义原表示与分布式词向量结合的研究。 **边界：**属于表示学习，不是辞书RAG应用。

**本轮访问：**元数据、摘要及正文相关段落。

### [10] TEI Lex-0: A baseline encoding for lexicographic data

TASOVAC T, ROMARY L, SALGADO A. TEI Lex-0: A baseline encoding for lexicographic data[R/OL]. ELEXIS – European Lexicographic Infrastructure, 2018. [原始来源](https://novaresearch.unl.pt/en/publications/tei-lex-0-a-baseline-encoding-for-lexicographic-data/).

**主题／身份：**辞书编码；技术报告／社区规范。

**写作用途：**说明异构辞书机器可读编码及互操作性。 **边界：**技术建议／报告；统一格式不自动完成语义对齐。

**本轮访问：**机构书目与摘要。 [补充核验入口](https://dariah-eric.github.io/lexicalresources/pages/TEILex0/TEILex0.html)。

### [11] Lexicon Model for Ontologies: Community Report, 10 May 2016

CIMIANO P, MCCRAE J P, BUITELAAR P, eds. Lexicon Model for Ontologies: Community Report, 10 May 2016[R/OL]. W3C Ontology-Lexicon Community Group, 2016. [原始来源](https://www.w3.org/2016/05/ontolex/).

**主题／身份：**词汇链接模型；社区规范。

**写作用途：**区分词条、词形、义项与引用，说明semantics by reference。 **边界：**社区最终报告，不是W3C Recommendation；不是完整形式语义理论。

**本轮访问：**原规范第2节及第3节相关定义。

### [12] GDEX: Automatically Finding Good Dictionary Examples in a Corpus

KILGARRIFF A, HUSÁK M, MCADAM K, et al. GDEX: Automatically Finding Good Dictionary Examples in a Corpus[C]. Proceedings of the 13th EURALEX International Congress: 425–432, 2008. [原始来源](https://euralex.org/publications/gdex-automatically-finding-good-dictionary-examples-in-a-corpus/).

**主题／身份：**语料库辅助编纂；已发表论文。

**写作用途：**连接语料例句检索、质量筛选与编纂者选择。 **边界：**选择真实语料例证不同于生成新例句。

**本轮访问：**元数据与摘要。

### [13] WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations

PILEHVAR M T, CAMACHO-COLLADOS J. WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations[C]. Proceedings of NAACL-HLT 2019, Volume 1: 1267–1273, 2019. [原始来源](https://aclanthology.org/N19-1128/). DOI: 10.18653/v1/N19-1128.

**主题／身份：**语境词义评测；已发表论文。

**写作用途：**说明无需输出统一义项ID的语义区分任务。 **边界：**二元语境判断不等于跨辞书宽窄关系标注。

**本轮访问：**元数据与摘要。

### [14] Definition Modeling: Learning to Define Word Embeddings in Natural Language

NORASET T, LIANG C, BIRNBAUM L, et al. Definition Modeling: Learning to Define Word Embeddings in Natural Language[C]. Proceedings of the AAAI Conference on Artificial Intelligence, 31(1), 2017. [原始来源](https://ojs.aaai.org/index.php/AAAI/article/view/10996). DOI: 10.1609/aaai.v31i1.10996.

**主题／身份：**释义生成；已发表论文。

**写作用途：**交代由词表示生成自然语言解释的早期路径。 **边界：**不是由外部检索证据支持的RAG。

**本轮访问：**元数据与摘要。

### [15] WantWords: An Open-source Online Reverse Dictionary System

QI F, ZHANG L, YANG Y, et al. WantWords: An Open-source Online Reverse Dictionary System[C]. Proceedings of EMNLP 2020: System Demonstrations: 175–181, 2020. [原始来源](https://aclanthology.org/2020.emnlp-demos.23/). DOI: 10.18653/v1/2020.emnlp-demos.23.

**主题／身份：**逆向词典；已发表论文。

**写作用途：**支持中英文及跨语言的描述到词语检索。 **边界：**返回候选词，不是从检索证据生成综合答案。

**本轮访问：**元数据与摘要。

### [16] Definition Modelling for Appropriate Specificity

HUANG H, KAJIWARA T, ARASE Y. Definition Modelling for Appropriate Specificity[C]. Proceedings of EMNLP 2021: 2499–2509, 2021. [原始来源](https://aclanthology.org/2021.emnlp-main.194/). DOI: 10.18653/v1/2021.emnlp-main.194.

**主题／身份：**释义粒度；已发表论文。

**写作用途：**讨论生成释义过宽／过窄与适切具体性。 **边界：**不把任意更长的释义视为更准确。

**本轮访问：**元数据与摘要。

### [17] Interpretable Word Sense Representations via Definition Generation: The Case of Semantic Change Analysis

GIULIANELLI M, LUDEN I, FERNÁNDEZ R, et al. Interpretable Word Sense Representations via Definition Generation: The Case of Semantic Change Analysis[C]. Proceedings of ACL 2023, Volume 1: 3130–3148, 2023. [原始来源](https://aclanthology.org/2023.acl-long.176/). DOI: 10.18653/v1/2023.acl-long.176.

**主题／身份：**释义作为表示；已发表论文。

**写作用途：**自然语言定义可作为可解释的语义分析对象。 **边界：**语义变化任务上的证据，不是辞书RAG效果证明。

**本轮访问：**元数据与摘要。

### [18] Low-Cost Generation and Evaluation of Dictionary Example Sentences

CAI B, CLARENCE N, LIANG D, et al. Low-Cost Generation and Evaluation of Dictionary Example Sentences[C]. Proceedings of NAACL-HLT 2024, Volume 1: 3538–3549, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.194/). DOI: 10.18653/v1/2024.naacl-long.194.

**主题／身份：**例句生成；已发表论文。

**写作用途：**连接低成本生成、自动选择与例句评估。 **边界：**特定评价设置下的结果，不等于所有例句可直接入典。

**本轮访问：**元数据与摘要。

### [19] 例句质量评估体系构建及大语言模型例句生成能力评估

方明炜, 朱君辉, 鲁鹿鸣, 等. 例句质量评估体系构建及大语言模型例句生成能力评估[C]. 第二十四届中国计算语言学大会论文集: 117–130, 2025. [原始来源](https://aclanthology.org/2025.ccl-1.10/).

**主题／身份：**中文例句质量；已发表论文。

**写作用途：**用规范性、语境独立性、典型度等维度评价教学例句。 **边界：**分类器准确率不是LLM生成例句正确率。

**本轮访问：**元数据、原文首页图像及摘要。

### [20] Do Large Language Models Understand Word Senses?

MECONI D, STIRPE S, MARTELLI F, et al. Do Large Language Models Understand Word Senses?[C]. Proceedings of EMNLP 2025: 33897–33916, 2025. [原始来源](https://aclanthology.org/2025.emnlp-main.1720/). DOI: 10.18653/v1/2025.emnlp-main.1720.

**主题／身份：**LLM词义能力；已发表论文。

**写作用途：**强模型在受测WSD与生成任务上的表现应作为基线背景。 **边界：**任务、语言、版本有边界；不能概括为完全理解所有词义。

**本轮访问：**元数据与摘要。

### [21] Enhancing Lexical Relation Mining with Structured Sememe Knowledge

WANG H, LIANG Q, WANG Y, et al. Enhancing Lexical Relation Mining with Structured Sememe Knowledge[C]. Proceedings of ACL 2026, Volume 1: 4930–4947, 2026. [原始来源](https://aclanthology.org/2026.acl-long.224/). DOI: 10.18653/v1/2026.acl-long.224.

**主题／身份：**结构义原与关系挖掘；已发表论文。

**写作用途：**STC构树、关系图编码与预训练模型融合。 **边界：**SememeLRM验证模型内结构融合，不是词典RAG或API提示效果。

**本轮访问：**元数据、正文方法与实验设置相关段落。

### [22] Dense Passage Retrieval for Open-Domain Question Answering

KARPUKHIN V, OGUZ B, MIN S, et al. Dense Passage Retrieval for Open-Domain Question Answering[C]. Proceedings of EMNLP 2020: 6769–6781, 2020. [原始来源](https://aclanthology.org/2020.emnlp-main.550/). DOI: 10.18653/v1/2020.emnlp-main.550.

**主题／身份：**稠密检索；已发表论文。

**写作用途：**说明双编码器语义检索与段落召回。 **边界：**相关性分数不等于义项等价判断。

**本轮访问：**元数据与摘要。

### [23] Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions

TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions[C]. Proceedings of ACL 2023, Volume 1: 10014–10037, 2023. [原始来源](https://aclanthology.org/2023.acl-long.557/). DOI: 10.18653/v1/2023.acl-long.557.

**主题／身份：**迭代检索；已发表论文。

**写作用途：**IRCoT使检索与中间推理交替。 **边界：**通用问答机制可借鉴，不等于辞书场景已获同样收益。

**本轮访问：**元数据、正文方法相关段落。

### [24] Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

ASAI A, WU Z, WANG Y, et al. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html).

**主题／身份：**检索与自反思；已发表论文。

**写作用途：**按需检索及生成质量评价的联合机制。 **边界：**训练反思标记；不能写成纯提示、完全无训练的方法。

**本轮访问：**元数据与摘要。

### [25] Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity

JEONG S, BAEK J, CHO S, et al. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity[C]. Proceedings of NAACL-HLT 2024, Volume 1: 7036–7050, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.389/). DOI: 10.18653/v1/2024.naacl-long.389.

**主题／身份：**适应性检索；已发表论文。

**写作用途：**小模型按问题复杂度选择无／单步／多步检索。 **边界：**控制分类器需要训练，不是零成本路由。

**本轮访问：**元数据与摘要。

### [26] Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph

SUN J, XU C, TANG L, et al. Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html).

**主题／身份：**知识图谱检索；已发表论文。

**写作用途：**LLM引导实体／关系路径探索。 **边界：**预先已有图及正确链接很重要；不能把所有图路径当证明。

**本轮访问：**元数据与摘要。

### [27] From Local to Global: A Graph RAG Approach to Query-Focused Summarization

EDGE D, TRINH H, CHENG N, et al. From Local to Global: A Graph RAG Approach to Query-Focused Summarization[EB/OL]. arXiv:2404.16130v2（初版2024；本清单采用2025修订版）, 2025. [原始来源](https://arxiv.org/abs/2404.16130v2). DOI: 10.48550/arXiv.2404.16130.

**主题／身份：**图RAG与全局综合；预印本。

**写作用途：**实体图、社区摘要与面向全局问题的回答。 **边界：**此处按所核验预印本著录；社区全局综合不同于义项导航。

**本轮访问：**预印本元数据与摘要、作者机构介绍。

### [28] HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

JIMÉNEZ GUTIÉRREZ B, SHU Y, GU Y, et al. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models[C]. Advances in Neural Information Processing Systems, 37, 2024. [原始来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6ddc001d07ca4f319af96a3024f6dbd1-Abstract.html).

**主题／身份：**图记忆与关联检索；已发表论文。

**写作用途：**结合知识图结构与个性化PageRank做关联检索。 **边界：**一次图检索可覆盖多步关联，不宜按API次数定义推理跳数。

**本轮访问：**元数据与摘要。

### [29] Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language

MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).

**主题／身份：**辞书RAG直接应用；已发表论文。

**写作用途：**词典条目与检索平行句共同帮助低资源语言翻译。 **边界：**特定语言、资料和样本，不能直接推广到中文义项推理。

**本轮访问：**正文第3—4节、实验讨论相关段落。

### [30] Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith

ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.

**主题／身份：**历史辞书RAG直接应用；预印本。

**写作用途：**历史词典、混合检索、重排和意图路由的结合。 **边界：**预印本；含训练组件，模型裁判和人工核验仍受样本限制。

**本轮访问：**正文意图路由、训练设置、结论相关段落。

### [31] Enabling Large Language Models to Generate Text with Citations

GAO T, YEN H, YU J, et al. Enabling Large Language Models to Generate Text with Citations[C]. Proceedings of EMNLP 2023: 6465–6488, 2023. [原始来源](https://aclanthology.org/2023.emnlp-main.398/). DOI: 10.18653/v1/2023.emnlp-main.398.

**主题／身份：**引用与证据评价；已发表论文。

**写作用途：**ALCE分开评价内容与引用质量。 **边界：**附有引用不等于每条断言都被该引用支持。

**本轮访问：**元数据与摘要。

### [32] RAGAs: Automated Evaluation of Retrieval Augmented Generation

ES S, JAMES J, ESPINOSA ANKE L, et al. RAGAs: Automated Evaluation of Retrieval Augmented Generation[C]. Proceedings of EACL 2024: System Demonstrations: 150–158, 2024. [原始来源](https://aclanthology.org/2024.eacl-demo.16/). DOI: 10.18653/v1/2024.eacl-demo.16.

**主题／身份：**RAG自动评估；已发表论文。

**写作用途：**区分检索上下文、忠实性和回答质量。 **边界：**reference-free不等于无假设，更不是免除人工gold。

**本轮访问：**元数据与摘要。

### [33] Lost in the Middle: How Language Models Use Long Contexts

LIU N F, LIN K, HEWITT J, et al. Lost in the Middle: How Language Models Use Long Contexts[J]. Transactions of the Association for Computational Linguistics, 12: 157–173, 2024. [原始来源](https://aclanthology.org/2024.tacl-1.9/). DOI: 10.1162/tacl_a_00638.

**主题／身份：**上下文利用；已发表论文。

**写作用途：**说明证据长度与排列影响模型利用信息。 **边界：**发现来自受测模型与任务，不能断言所有新模型永远相同。

**本轮访问：**元数据与摘要。

### [34] ♫ MuSiQue: Multihop Questions via Single-hop Question Composition

TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. ♫ MuSiQue: Multihop Questions via Single-hop Question Composition[J]. Transactions of the Association for Computational Linguistics, 10: 539–554, 2022. [原始来源](https://aclanthology.org/2022.tacl-1.31/). DOI: 10.1162/tacl_a_00475.

**主题／身份：**多跳评测；已发表论文。

**写作用途：**以步骤间真实信息依赖检查所谓多跳。 **边界：**一般QA基准，不是现成辞书测试集。

**本轮访问：**元数据与摘要。

### [35] Survey Article: Inter-Coder Agreement for Computational Linguistics

ARTSTEIN R, POESIO M. Survey Article: Inter-Coder Agreement for Computational Linguistics[J]. Computational Linguistics, 34(4): 555–596, 2008. [原始来源](https://aclanthology.org/J08-4004/). DOI: 10.1162/coli.07-034-R2.

**主题／身份：**人工标注评价；已发表论文。

**写作用途：**选择适合任务尺度的标注一致性统计。 **边界：**不规定所有任务统一合格阈值。

**本轮访问：**正式论文元数据及正文概述。

## 中文拓展阅读（未作为正文证据）

柳长青. 数字辞书智能化编纂：大语言模型的创新应用[M]. 北京：商务印书馆，2026. ISBN 978-7-100-26263-7. [出版社书目页](https://www.cp.com.cn/book/ac345f62-c.html)。

本轮仅核验出版社书目与介绍，未取得全书，不以它支持具体实验或章节论断。适合经图书馆取得后补充中文辞书学的理论和实践语境；不计入上述35项及初稿引用编号。

## 引用时容易出错的地方

OpenHowNet在本清单按2019预印本著录；RAG、DPR是2020正式论文。Self-RAG是ICLR 2024，而不是将2023预印本年误当正式发表年。GraphRAG初版2024，但本清单明确采用2025 v2。多哈历史辞书RAG为2026预印本。SememeLRM已核对ACL 2026条目，不能仍写成未发表设想。OntoLex是社区报告，不是W3C Recommendation。CCL 2025例句研究中98.6%是其机器学习评价模型的指标，不能写成LLM生成例句正确率。词典RAG直接应用、通用RAG方法及语义表示研究分别归类，不互相替代证据。
