# 配套PPT逐页讲稿

正文23页，参考文献附录4页；建议正文约17—20分钟，附录按需展示。

内容依据：`03_draft.md`（来源提交 `fe0e149ccc88b4ae9d371bb2397c197be8106e79`）。文献范围沿用初稿截至2026-09-22的清单；本次未新增外部研究。

## 01 辞书知识与检索增强生成的融合

对应初稿：摘要／全文；建议20秒。

今天汇报的主题是辞书、词汇语义与检索增强生成的融合。汇报按照已有初稿展开，依次讨论为什么需要融合、有哪些技术路径、直接应用能支持什么结论以及未来需要解决的问题。这是主题式文献综述，不是新模型实验报告。



## 02 三个问题，串起整篇综述

对应初稿：§1；建议45秒。

全文围绕三个问题展开，而不是按照模型名称罗列文献。第一个问题是动因，第二个是技术如何分工，第三个是证据是否足以支持发展判断。本文的中心论点是：有更多可检索文本还不够，系统还需要区分义项、保留来源并说明答案依据。后面的每项技术都放回这条论证链中讨论。

[1] DE SCHRYVER G M. Lexicographers’ Dreams in the Electronic-Dictionary Age[J]. International Journal of Lexicography, 16(2): 143–199, 2003. [原始来源](https://doi.org/10.1093/ijl/16.2.143). DOI: 10.1093/ijl/16.2.143.
[2] DE SCHRYVER G M. Generative AI and Lexicography: The Current State of the Art Using ChatGPT[J]. International Journal of Lexicography, 36(4): 355–387, 2023. [原始来源](https://doi.org/10.1093/ijl/ecad021). DOI: 10.1093/ijl/ecad021.
[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).

## 03 先区分证据层次，再评价技术发展

对应初稿：§1.1；建议45秒。

初稿重点覆盖2020—2026年的研究，同时回溯电子辞书和语义资源的基础工作，原清单检索截止2026年9月22日。本次PPT只是对现有初稿的转述，没有扩大文献检索。正式论文、预印本和社区报告分别标注；阅读深度仍以参考清单为准。通用检索论文不能直接充当辞书专用系统的性能证据。

[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).
[5] MILLER G A. WordNet: A Lexical Database for English[J]. Communications of the ACM, 38(11): 39–41, 1995. [原始来源](https://doi.org/10.1145/219717.219748). DOI: 10.1145/219717.219748.
[11] CIMIANO P, MCCRAE J P, BUITELAAR P, eds. Lexicon Model for Ontologies: Community Report, 10 May 2016[R/OL]. W3C Ontology-Lexicon Community Group, 2016. [原始来源](https://www.w3.org/2016/05/ontolex/).
[21] WANG H, LIANG Q, WANG Y, et al. Enhancing Lexical Relation Mining with Structured Sememe Knowledge[C]. Proceedings of ACL 2026, Volume 1: 4930–4947, 2026. [原始来源](https://aclanthology.org/2026.acl-long.224/). DOI: 10.18653/v1/2026.acl-long.224.
[23] TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions[C]. Proceedings of ACL 2023, Volume 1: 10014–10037, 2023. [原始来源](https://aclanthology.org/2023.acl-long.557/). DOI: 10.18653/v1/2023.acl-long.557.
[29] MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).
[30] ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.

## 04 融合动因：三种需求同时发生变化

对应初稿：§1／§3.1；建议40秒。

数字化改善访问路径，生成模型扩展交互方式，辞书知识则可以为模型提供有来源的词汇证据。这三种变化是互补的。不能据此认为模型完全不懂词义，也不能因为辞书经过编纂就忽略版本、语境和分义差异。融合的动因是让解释更适合问题并能够回查，而非简单替代现有辞书。

[1] DE SCHRYVER G M. Lexicographers’ Dreams in the Electronic-Dictionary Age[J]. International Journal of Lexicography, 16(2): 143–199, 2003. [原始来源](https://doi.org/10.1093/ijl/16.2.143). DOI: 10.1093/ijl/16.2.143.
[2] DE SCHRYVER G M. Generative AI and Lexicography: The Current State of the Art Using ChatGPT[J]. International Journal of Lexicography, 36(4): 355–387, 2023. [原始来源](https://doi.org/10.1093/ijl/ecad021). DOI: 10.1093/ijl/ecad021.
[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).
[15] QI F, ZHANG L, YANG Y, et al. WantWords: An Open-source Online Reverse Dictionary System[C]. Proceedings of EMNLP 2020: System Demonstrations: 175–181, 2020. [原始来源](https://aclanthology.org/2020.emnlp-demos.23/). DOI: 10.18653/v1/2020.emnlp-demos.23.

## 05 发展脉络：多条路线汇合，而非逐代替代

对应初稿：§2—§5；建议40秒。

这张图是按综述主题整理的时间线，不是技术优劣排名。语义网络、编码规范、语料例证和生成式交互并不是互相替代的关系。较早的资源与规范仍然为较新的检索增强系统提供基础。后面将分别说明这些路线解决的是表示、存储、选择证据还是组织回答。

[1] DE SCHRYVER G M. Lexicographers’ Dreams in the Electronic-Dictionary Age[J]. International Journal of Lexicography, 16(2): 143–199, 2003. [原始来源](https://doi.org/10.1093/ijl/16.2.143). DOI: 10.1093/ijl/16.2.143.
[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
[5] MILLER G A. WordNet: A Lexical Database for English[J]. Communications of the ACM, 38(11): 39–41, 1995. [原始来源](https://doi.org/10.1145/219717.219748). DOI: 10.1145/219717.219748.
[6] BAKER C F, FILLMORE C J, LOWE J B. The Berkeley FrameNet Project[C]. 36th Annual Meeting of the ACL and 17th International Conference on Computational Linguistics, Volume 1: 86–90, 1998. [原始来源](https://aclanthology.org/P98-1013/). DOI: 10.3115/980845.980860.
[7] NAVIGLI R, PONZETTO S P. BabelNet: Building a Very Large Multilingual Semantic Network[C]. Proceedings of ACL 2010: 216–225, 2010. [原始来源](https://aclanthology.org/P10-1023/).
[10] TASOVAC T, ROMARY L, SALGADO A. TEI Lex-0: A baseline encoding for lexicographic data[R/OL]. ELEXIS – European Lexicographic Infrastructure, 2018. [原始来源](https://novaresearch.unl.pt/en/publications/tei-lex-0-a-baseline-encoding-for-lexicographic-data/).
[11] CIMIANO P, MCCRAE J P, BUITELAAR P, eds. Lexicon Model for Ontologies: Community Report, 10 May 2016[R/OL]. W3C Ontology-Lexicon Community Group, 2016. [原始来源](https://www.w3.org/2016/05/ontolex/).
[12] KILGARRIFF A, HUSÁK M, MCADAM K, et al. GDEX: Automatically Finding Good Dictionary Examples in a Corpus[C]. Proceedings of the 13th EURALEX International Congress: 425–432, 2008. [原始来源](https://euralex.org/publications/gdex-automatically-finding-good-dictionary-examples-in-a-corpus/).
[14] NORASET T, LIANG C, BIRNBAUM L, et al. Definition Modeling: Learning to Define Word Embeddings in Natural Language[C]. Proceedings of the AAAI Conference on Artificial Intelligence, 31(1), 2017. [原始来源](https://ojs.aaai.org/index.php/AAAI/article/view/10996). DOI: 10.1609/aaai.v31i1.10996.
[15] QI F, ZHANG L, YANG Y, et al. WantWords: An Open-source Online Reverse Dictionary System[C]. Proceedings of EMNLP 2020: System Demonstrations: 175–181, 2020. [原始来源](https://aclanthology.org/2020.emnlp-demos.23/). DOI: 10.18653/v1/2020.emnlp-demos.23.
[16] HUANG H, KAJIWARA T, ARASE Y. Definition Modelling for Appropriate Specificity[C]. Proceedings of EMNLP 2021: 2499–2509, 2021. [原始来源](https://aclanthology.org/2021.emnlp-main.194/). DOI: 10.18653/v1/2021.emnlp-main.194.
[17] GIULIANELLI M, LUDEN I, FERNÁNDEZ R, et al. Interpretable Word Sense Representations via Definition Generation: The Case of Semantic Change Analysis[C]. Proceedings of ACL 2023, Volume 1: 3130–3148, 2023. [原始来源](https://aclanthology.org/2023.acl-long.176/). DOI: 10.18653/v1/2023.acl-long.176.
[29] MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).
[30] ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.

## 06 语义资源的关键差异：表示单位不同

对应初稿：§2.1；建议55秒。

WordNet侧重同义词集和词汇关系，FrameNet强调情境中的参与者结构，BabelNet扩展多语言与百科覆盖，HowNet式资源刻画意义成分。它们的单位和目的不同，因此不宜混成一个统一分类表。OpenHowNet在本文按原清单所列预印本和资源入口引用。显式结构有利于解释关系，向量表示则有利于发现词面不同的候选。

[5] MILLER G A. WordNet: A Lexical Database for English[J]. Communications of the ACM, 38(11): 39–41, 1995. [原始来源](https://doi.org/10.1145/219717.219748). DOI: 10.1145/219717.219748.
[6] BAKER C F, FILLMORE C J, LOWE J B. The Berkeley FrameNet Project[C]. 36th Annual Meeting of the ACL and 17th International Conference on Computational Linguistics, Volume 1: 86–90, 1998. [原始来源](https://aclanthology.org/P98-1013/). DOI: 10.3115/980845.980860.
[7] NAVIGLI R, PONZETTO S P. BabelNet: Building a Very Large Multilingual Semantic Network[C]. Proceedings of ACL 2010: 216–225, 2010. [原始来源](https://aclanthology.org/P10-1023/).
[8] QI F, YANG C, LIU Z, et al. OpenHowNet: An Open Sememe-based Lexical Knowledge Base[EB/OL]. arXiv:1901.09957, 2019. [原始来源](https://arxiv.org/abs/1901.09957). DOI: 10.48550/arXiv.1901.09957.
[9] 于宁, 王江萍, 石宇, 等. 基于义原表示学习的词向量表示方法[C]. 第二十届中国计算语言学大会论文集: 57–65, 2021. [原始来源](https://aclanthology.org/2021.ccl-1.6/).

## 07 统一格式 ≠ 统一意义

对应初稿：§2.2／§4.1；建议45秒。

把两本辞书转成相同JSON字段，并不会消除它们的编号、分义粒度或解释差异。TEI Lex-0和OntoLex解决编码与关联组织问题，MWSA把义项对应作为独立任务。需要特别说明，OntoLex在本文引用的是社区报告，不是W3C标准建议。本文据此建议保留原文和来源编号，再建立可复核的映射。

[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).
[10] TASOVAC T, ROMARY L, SALGADO A. TEI Lex-0: A baseline encoding for lexicographic data[R/OL]. ELEXIS – European Lexicographic Infrastructure, 2018. [原始来源](https://novaresearch.unl.pt/en/publications/tei-lex-0-a-baseline-encoding-for-lexicographic-data/).
[11] CIMIANO P, MCCRAE J P, BUITELAAR P, eds. Lexicon Model for Ontologies: Community Report, 10 May 2016[R/OL]. W3C Ontology-Lexicon Community Group, 2016. [原始来源](https://www.w3.org/2016/05/ontolex/).
[22] KARPUKHIN V, OGUZ B, MIN S, et al. Dense Passage Retrieval for Open-Domain Question Answering[C]. Proceedings of EMNLP 2020: 6769–6781, 2020. [原始来源](https://aclanthology.org/2020.emnlp-main.550/). DOI: 10.18653/v1/2020.emnlp-main.550.

## 08 定义、例证、语境：不能混成同一种文本

对应初稿：§2.3；建议40秒。

GDEX体现的是从语料中筛选好例句，而生成例句首先是候选解释材料，两者的证据身份不同。WiC说明比较语境中的词义可以不要求输出统一编号，但二元同异义判断不能取代所有跨辞书关系。辞书数据库应该允许模型知道自己看到的是定义、例证还是使用语境，而不是一律当作相同的文本块。

[12] KILGARRIFF A, HUSÁK M, MCADAM K, et al. GDEX: Automatically Finding Good Dictionary Examples in a Corpus[C]. Proceedings of the 13th EURALEX International Congress: 425–432, 2008. [原始来源](https://euralex.org/publications/gdex-automatically-finding-good-dictionary-examples-in-a-corpus/).
[13] PILEHVAR M T, CAMACHO-COLLADOS J. WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations[C]. Proceedings of NAACL-HLT 2019, Volume 1: 1267–1273, 2019. [原始来源](https://aclanthology.org/N19-1128/). DOI: 10.18653/v1/N19-1128.
[18] CAI B, CLARENCE N, LIANG D, et al. Low-Cost Generation and Evaluation of Dictionary Example Sentences[C]. Proceedings of NAACL-HLT 2024, Volume 1: 3538–3549, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.194/). DOI: 10.18653/v1/2024.naacl-long.194.
[19] 方明炜, 朱君辉, 鲁鹿鸣, 等. 例句质量评估体系构建及大语言模型例句生成能力评估[C]. 第二十四届中国计算语言学大会论文集: 117–130, 2025. [原始来源](https://aclanthology.org/2025.ccl-1.10/).

## 09 大语言模型与辞书：两种作用方向

对应初稿：§3.1—§3.2；建议45秒。

左边是编纂和语言服务的候选生成，右边是用既有辞书知识增强回答。WantWords从描述寻找词语，与从词向量生成定义的方向不同；它们也不因涉及检索或语言模型就自动构成RAG。区分这两种作用方向，可以避免把生成能力强直接解释成证据使用可靠。

[2] DE SCHRYVER G M. Generative AI and Lexicography: The Current State of the Art Using ChatGPT[J]. International Journal of Lexicography, 36(4): 355–387, 2023. [原始来源](https://doi.org/10.1093/ijl/ecad021). DOI: 10.1093/ijl/ecad021.
[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
[14] NORASET T, LIANG C, BIRNBAUM L, et al. Definition Modeling: Learning to Define Word Embeddings in Natural Language[C]. Proceedings of the AAAI Conference on Artificial Intelligence, 31(1), 2017. [原始来源](https://ojs.aaai.org/index.php/AAAI/article/view/10996). DOI: 10.1609/aaai.v31i1.10996.
[15] QI F, ZHANG L, YANG Y, et al. WantWords: An Open-source Online Reverse Dictionary System[C]. Proceedings of EMNLP 2020: System Demonstrations: 175–181, 2020. [原始来源](https://aclanthology.org/2020.emnlp-demos.23/). DOI: 10.18653/v1/2020.emnlp-demos.23.
[18] CAI B, CLARENCE N, LIANG D, et al. Low-Cost Generation and Evaluation of Dictionary Example Sentences[C]. Proceedings of NAACL-HLT 2024, Volume 1: 3538–3549, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.194/). DOI: 10.18653/v1/2024.naacl-long.194.
[19] 方明炜, 朱君辉, 鲁鹿鸣, 等. 例句质量评估体系构建及大语言模型例句生成能力评估[C]. 第二十四届中国计算语言学大会论文集: 117–130, 2025. [原始来源](https://aclanthology.org/2025.ccl-1.10/).

## 10 质量转向：从“像一句话”到“解释得恰当”

对应初稿：§3.1—§3.3；建议45秒。

释义生成不只是写出通顺句子，还涉及解释的具体程度。例句评价也不能只看语法，中文教学研究给出了五个相关维度。与此同时，词义能力研究说明强模型本身已经是重要基线。因此，外部知识的意义应通过困难语义条件和可靠性来检验，而不能建立在模型一概不懂词义的前提上。

[16] HUANG H, KAJIWARA T, ARASE Y. Definition Modelling for Appropriate Specificity[C]. Proceedings of EMNLP 2021: 2499–2509, 2021. [原始来源](https://aclanthology.org/2021.emnlp-main.194/). DOI: 10.18653/v1/2021.emnlp-main.194.
[17] GIULIANELLI M, LUDEN I, FERNÁNDEZ R, et al. Interpretable Word Sense Representations via Definition Generation: The Case of Semantic Change Analysis[C]. Proceedings of ACL 2023, Volume 1: 3130–3148, 2023. [原始来源](https://aclanthology.org/2023.acl-long.176/). DOI: 10.18653/v1/2023.acl-long.176.
[18] CAI B, CLARENCE N, LIANG D, et al. Low-Cost Generation and Evaluation of Dictionary Example Sentences[C]. Proceedings of NAACL-HLT 2024, Volume 1: 3538–3549, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.194/). DOI: 10.18653/v1/2024.naacl-long.194.
[19] 方明炜, 朱君辉, 鲁鹿鸣, 等. 例句质量评估体系构建及大语言模型例句生成能力评估[C]. 第二十四届中国计算语言学大会论文集: 117–130, 2025. [原始来源](https://aclanthology.org/2025.ccl-1.10/).
[20] MECONI D, STIRPE S, MARTELLI F, et al. Do Large Language Models Understand Word Senses?[C]. Proceedings of EMNLP 2025: 33897–33916, 2025. [原始来源](https://aclanthology.org/2025.emnlp-main.1720/). DOI: 10.18653/v1/2025.emnlp-main.1720.

## 11 结构知识进入模型，至少有三种位置

对应初稿：§3.3；建议45秒。

初稿以SememeLRM作为结构知识进入模型的案例：义原树经关系图编码与预训练语言模型结合，任务是词汇关系分类和蕴含。它不能直接证明把同样结构放进生成提示就有相同收益。这张表概括不同知识接入位置，各方式可以组合，但必须按实际训练和实验设置描述。

[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
[9] 于宁, 王江萍, 石宇, 等. 基于义原表示学习的词向量表示方法[C]. 第二十届中国计算语言学大会论文集: 57–65, 2021. [原始来源](https://aclanthology.org/2021.ccl-1.6/).
[21] WANG H, LIANG Q, WANG Y, et al. Enhancing Lexical Relation Mining with Structured Sememe Knowledge[C]. Proceedings of ACL 2026, Volume 1: 4930–4947, 2026. [原始来源](https://aclanthology.org/2026.acl-long.224/). DOI: 10.18653/v1/2026.acl-long.224.
[23] TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions[C]. Proceedings of ACL 2023, Volume 1: 10014–10037, 2023. [原始来源](https://aclanthology.org/2023.acl-long.557/). DOI: 10.18653/v1/2023.acl-long.557.
[26] SUN J, XU C, TANG L, et al. Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html).

## 12 RAG的关键链条：取证、组织、生成、回查

对应初稿：§4.1／§6.1；建议45秒。

RAG将外部检索证据引入生成过程。Lewis等的奠基工作包含任务训练，因此不能把RAG一概理解为完全不训练。对于辞书应用，必须先确定检索单位，再判断取回内容是否支持当前问题。末端还需要回查断言与引用，不能只因为输出附了链接就认为内容已经可靠。

[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
[22] KARPUKHIN V, OGUZ B, MIN S, et al. Dense Passage Retrieval for Open-Domain Question Answering[C]. Proceedings of EMNLP 2020: 6769–6781, 2020. [原始来源](https://aclanthology.org/2020.emnlp-main.550/). DOI: 10.18653/v1/2020.emnlp-main.550.
[31] GAO T, YEN H, YU J, et al. Enabling Large Language Models to Generate Text with Citations[C]. Proceedings of EMNLP 2023: 6465–6488, 2023. [原始来源](https://aclanthology.org/2023.emnlp-main.398/). DOI: 10.18653/v1/2023.emnlp-main.398.
[32] ES S, JAMES J, ESPINOSA ANKE L, et al. RAGAs: Automated Evaluation of Retrieval Augmented Generation[C]. Proceedings of EACL 2024: System Demonstrations: 150–158, 2024. [原始来源](https://aclanthology.org/2024.eacl-demo.16/). DOI: 10.18653/v1/2024.eacl-demo.16.

## 13 检索粒度应由问题决定

对应初稿：§4.1；建议45秒。

本页是初稿的综合建议，不是已经得到统一效果证明的最佳检索方案。整词条、义项、片段和例证都有适用条件。可结合词形、读音等精确线索，语义召回和义项级重排；重排要判断是否支持当前问题，而不是只追求文本相似。原始记录保持完整，模型每次接收多少信息则按任务控制。

[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).
[13] PILEHVAR M T, CAMACHO-COLLADOS J. WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations[C]. Proceedings of NAACL-HLT 2019, Volume 1: 1267–1273, 2019. [原始来源](https://aclanthology.org/N19-1128/). DOI: 10.18653/v1/N19-1128.
[22] KARPUKHIN V, OGUZ B, MIN S, et al. Dense Passage Retrieval for Open-Domain Question Answering[C]. Proceedings of EMNLP 2020: 6769–6781, 2020. [原始来源](https://aclanthology.org/2020.emnlp-main.550/). DOI: 10.18653/v1/2020.emnlp-main.550.

## 14 按需检索：控制“何时查、是否再查”

对应初稿：§4.2；建议55秒。

IRCoT、Self-RAG和Adaptive-RAG都关注检索适应性，但不能统一称为无训练提示方法。迁移到辞书场景时，简单查字音和复杂历时比较不应执行相同流程。初稿建议在资料足够时停止，只有未解释概念影响答案时再补取证据，同时考虑来源冲突与预算，而非只依赖模型自报信心。

[23] TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions[C]. Proceedings of ACL 2023, Volume 1: 10014–10037, 2023. [原始来源](https://aclanthology.org/2023.acl-long.557/). DOI: 10.18653/v1/2023.acl-long.557.
[24] ASAI A, WU Z, WANG Y, et al. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html).
[25] JEONG S, BAEK J, CHO S, et al. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity[C]. Proceedings of NAACL-HLT 2024, Volume 1: 7036–7050, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.389/). DOI: 10.18653/v1/2024.naacl-long.389.

## 15 图结构RAG不是一种统一算法

对应初稿：§4.3；建议55秒。

三种图方法的任务和机制不同。GraphRAG在本文沿用初稿所选2025修订预印本，初版为2024年。不能因为辞书也有链接，就假定实体图的统一节点方式可以直接照搬。词头可能多义，参见关系也不保证等价。对于信息已经充分的短定义，简单文本检索可能就够用，图结构是否增益需要具体比较。

[26] SUN J, XU C, TANG L, et al. Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html).
[27] EDGE D, TRINH H, CHENG N, et al. From Local to Global: A Graph RAG Approach to Query-Focused Summarization[EB/OL]. arXiv:2404.16130v2（初版2024；本清单采用2025修订版）, 2025. [原始来源](https://arxiv.org/abs/2404.16130v2). DOI: 10.48550/arXiv.2404.16130.
[28] JIMÉNEZ GUTIÉRREZ B, SHU Y, GU Y, et al. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models[C]. Advances in Neural Information Processing Systems, 37, 2024. [原始来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6ddc001d07ca4f319af96a3024f6dbd1-Abstract.html).

## 16 直接案例一：低资源语言翻译

对应初稿：§5.1；建议55秒。

这个案例直接把辞书内容用于生成时的外部知识，因此与本综述主题的联系比一般RAG论文更直接。其启示是，正确词条与合适例句本身就有价值，不必先建立庞大图谱。但词典覆盖、例句相关性和模型选择都会影响结果。初稿没有提取统一可比的性能数字，所以本页不补造或跨任务比较分数。

[29] MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).

## 17 直接案例二：历史语言理解

对应初稿：§5.2；建议55秒。

该工作以多哈历史辞书为来源，面向包括《古兰经》与圣训在内的历史语言材料，说明词汇知识不仅是现代概念解释，还包含时期与语境信息。这里概述的是技术任务，不对宗教内容作评价。论文含训练组件，也结合自动评价和人工核验，因此不能描述成无训练且无需人工的通用系统。

[30] ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.

## 18 已有证据支持什么，又没有支持什么？

对应初稿：§5.3；建议40秒。

本页集中回应综述的证据边界。直接案例表明不是没有前人，通用技术也提供了丰富工具；但两者之间仍需要辞书任务级适配。不能把相邻技术结果包装成直接辞书成果，也不应把不同指标拼成绝对排名。更审慎的判断是：局部可行性已有证据，普遍可靠性尚需分任务检验。

[21] WANG H, LIANG Q, WANG Y, et al. Enhancing Lexical Relation Mining with Structured Sememe Knowledge[C]. Proceedings of ACL 2026, Volume 1: 4930–4947, 2026. [原始来源](https://aclanthology.org/2026.acl-long.224/). DOI: 10.18653/v1/2026.acl-long.224.
[23] TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions[C]. Proceedings of ACL 2023, Volume 1: 10014–10037, 2023. [原始来源](https://aclanthology.org/2023.acl-long.557/). DOI: 10.18653/v1/2023.acl-long.557.
[24] ASAI A, WU Z, WANG Y, et al. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html).
[25] JEONG S, BAEK J, CHO S, et al. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity[C]. Proceedings of NAACL-HLT 2024, Volume 1: 7036–7050, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.389/). DOI: 10.18653/v1/2024.naacl-long.389.
[26] SUN J, XU C, TANG L, et al. Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html).
[27] EDGE D, TRINH H, CHENG N, et al. From Local to Global: A Graph RAG Approach to Query-Focused Summarization[EB/OL]. arXiv:2404.16130v2（初版2024；本清单采用2025修订版）, 2025. [原始来源](https://arxiv.org/abs/2404.16130v2). DOI: 10.48550/arXiv.2404.16130.
[28] JIMÉNEZ GUTIÉRREZ B, SHU Y, GU Y, et al. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models[C]. Advances in Neural Information Processing Systems, 37, 2024. [原始来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6ddc001d07ca4f319af96a3024f6dbd1-Abstract.html).
[29] MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).
[30] ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.

## 19 评价需要分层，不能只看答案是否流畅

对应初稿：§6.1／§7.4；建议50秒。

检索、生成和溯源必须分开，应用层则补充用户任务与成本。ALCE强调生成引用的评价，RAGAs区分上下文与回答质量，但自动裁判并不能替代全部辞书学判断。初稿提出的常用于正式场合与仅用于正式场合是说明性构造例子：流畅改写如果丢失强度差异，仍然可能改变解释。

[16] HUANG H, KAJIWARA T, ARASE Y. Definition Modelling for Appropriate Specificity[C]. Proceedings of EMNLP 2021: 2499–2509, 2021. [原始来源](https://aclanthology.org/2021.emnlp-main.194/). DOI: 10.18653/v1/2021.emnlp-main.194.
[19] 方明炜, 朱君辉, 鲁鹿鸣, 等. 例句质量评估体系构建及大语言模型例句生成能力评估[C]. 第二十四届中国计算语言学大会论文集: 117–130, 2025. [原始来源](https://aclanthology.org/2025.ccl-1.10/).
[31] GAO T, YEN H, YU J, et al. Enabling Large Language Models to Generate Text with Citations[C]. Proceedings of EMNLP 2023: 6465–6488, 2023. [原始来源](https://aclanthology.org/2023.emnlp-main.398/). DOI: 10.18653/v1/2023.emnlp-main.398.
[32] ES S, JAMES J, ESPINOSA ANKE L, et al. RAGAs: Automated Evaluation of Retrieval Augmented Generation[C]. Proceedings of EACL 2024: System Demonstrations: 150–158, 2024. [原始来源](https://aclanthology.org/2024.eacl-demo.16/). DOI: 10.18653/v1/2024.eacl-demo.16.
[35] ARTSTEIN R, POESIO M. Survey Article: Inter-Coder Agreement for Computational Linguistics[J]. Computational Linguistics, 34(4): 555–596, 2008. [原始来源](https://aclanthology.org/J08-4004/). DOI: 10.1162/coli.07-034-R2.

## 20 真正利用了证据，还是依靠模型猜对？

对应初稿：§6.2—§6.3；建议45秒。

Lost in the Middle在其受测任务和模型中发现信息位置影响表现，不应不加条件地推广到所有未来模型。MuSiQue则关注步骤之间真实的信息依赖。初稿据此建议通过证据移除、错义项替换和顺序变化检查使用过程。这些是评价设计建议，不代表本综述已经运行了这些实验。

[33] LIU N F, LIN K, HEWITT J, et al. Lost in the Middle: How Language Models Use Long Contexts[J]. Transactions of the Association for Computational Linguistics, 12: 157–173, 2024. [原始来源](https://aclanthology.org/2024.tacl-1.9/). DOI: 10.1162/tacl_a_00638.
[34] TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. ♫ MuSiQue: Multihop Questions via Single-hop Question Composition[J]. Transactions of the Association for Computational Linguistics, 10: 539–554, 2022. [原始来源](https://aclanthology.org/2022.tacl-1.31/). DOI: 10.1162/tacl_a_00475.
[35] ARTSTEIN R, POESIO M. Survey Article: Inter-Coder Agreement for Computational Linguistics[J]. Computational Linguistics, 34(4): 555–596, 2008. [原始来源](https://aclanthology.org/J08-4004/). DOI: 10.1162/coli.07-034-R2.

## 21 数据治理：来源、版本与使用条件

对应初稿：§6.3—§6.4；建议45秒。

本页讨论研究管理，不作特定司法辖区的法律判断。辞书内容经过编纂，仍可能在电子化过程中发生截断、乱码或编号错位。应修正机械错误，同时保留有意义的来源差异。是否可以读取、处理或公开再发布需要分别确认；模型产生的新解释也应保留生成身份。

[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).
[10] TASOVAC T, ROMARY L, SALGADO A. TEI Lex-0: A baseline encoding for lexicographic data[R/OL]. ELEXIS – European Lexicographic Infrastructure, 2018. [原始来源](https://novaresearch.unl.pt/en/publications/tei-lex-0-a-baseline-encoding-for-lexicographic-data/).
[11] CIMIANO P, MCCRAE J P, BUITELAAR P, eds. Lexicon Model for Ontologies: Community Report, 10 May 2016[R/OL]. W3C Ontology-Lexicon Community Group, 2016. [原始来源](https://www.w3.org/2016/05/ontolex/).
[35] ARTSTEIN R, POESIO M. Survey Article: Inter-Coder Agreement for Computational Linguistics[J]. Computational Linguistics, 34(4): 555–596, 2008. [原始来源](https://aclanthology.org/J08-4004/). DOI: 10.1162/coli.07-034-R2.

## 22 未来方向：可追溯的语义服务

对应初稿：§7；建议55秒。

四个方向沿用初稿的综合判断，不是已完成的新系统。来源义项组织关注证据责任，轻量检索关注收益与成本，生成验证协同保留编纂审核，跨语言评价检查可迁移性。共同目标是让辞书与模型分工合作：辞书提供有来源的词汇解释，模型帮助交互和组织，评价机制约束二者连接。

[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).
[11] CIMIANO P, MCCRAE J P, BUITELAAR P, eds. Lexicon Model for Ontologies: Community Report, 10 May 2016[R/OL]. W3C Ontology-Lexicon Community Group, 2016. [原始来源](https://www.w3.org/2016/05/ontolex/).
[16] HUANG H, KAJIWARA T, ARASE Y. Definition Modelling for Appropriate Specificity[C]. Proceedings of EMNLP 2021: 2499–2509, 2021. [原始来源](https://aclanthology.org/2021.emnlp-main.194/). DOI: 10.18653/v1/2021.emnlp-main.194.
[18] CAI B, CLARENCE N, LIANG D, et al. Low-Cost Generation and Evaluation of Dictionary Example Sentences[C]. Proceedings of NAACL-HLT 2024, Volume 1: 3538–3549, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.194/). DOI: 10.18653/v1/2024.naacl-long.194.
[19] 方明炜, 朱君辉, 鲁鹿鸣, 等. 例句质量评估体系构建及大语言模型例句生成能力评估[C]. 第二十四届中国计算语言学大会论文集: 117–130, 2025. [原始来源](https://aclanthology.org/2025.ccl-1.10/).
[24] ASAI A, WU Z, WANG Y, et al. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html).
[25] JEONG S, BAEK J, CHO S, et al. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity[C]. Proceedings of NAACL-HLT 2024, Volume 1: 7036–7050, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.389/). DOI: 10.18653/v1/2024.naacl-long.389.
[26] SUN J, XU C, TANG L, et al. Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html).
[29] MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).
[30] ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.
[31] GAO T, YEN H, YU J, et al. Enabling Large Language Models to Generate Text with Citations[C]. Proceedings of EMNLP 2023: 6465–6488, 2023. [原始来源](https://aclanthology.org/2023.emnlp-main.398/). DOI: 10.18653/v1/2023.emnlp-main.398.
[32] ES S, JAMES J, ESPINOSA ANKE L, et al. RAGAs: Automated Evaluation of Retrieval Augmented Generation[C]. Proceedings of EACL 2024: System Demonstrations: 150–158, 2024. [原始来源](https://aclanthology.org/2024.eacl-demo.16/). DOI: 10.18653/v1/2024.eacl-demo.16.
[35] ARTSTEIN R, POESIO M. Survey Article: Inter-Coder Agreement for Computational Linguistics[J]. Computational Linguistics, 34(4): 555–596, 2008. [原始来源](https://aclanthology.org/J08-4004/). DOI: 10.1162/coli.07-034-R2.

## 23 从“找到词条”到“可靠解释”

对应初稿：§8；建议35秒。

最后回到三个问题。数字辞书改变访问，语义资源帮助区分和连接意义，生成模型扩展表达方式，RAG引入外部证据。现有直接应用支持局部可行性，但不能自动推出全面成熟。值得追求的共同目标是：答案易于理解，同时能说明来源、适用条件及不确定性。可以请同学讨论：当不同辞书解释存在合理差异时，系统应该怎样呈现，而不是直接选一个覆盖其他来源？

[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).
[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).
[29] MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).
[30] ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.
[31] GAO T, YEN H, YU J, et al. Enabling Large Language Models to Generate Text with Citations[C]. Proceedings of EMNLP 2023: 6465–6488, 2023. [原始来源](https://aclanthology.org/2023.emnlp-main.398/). DOI: 10.18653/v1/2023.emnlp-main.398.
[32] ES S, JAMES J, ESPINOSA ANKE L, et al. RAGAs: Automated Evaluation of Retrieval Augmented Generation[C]. Proceedings of EACL 2024: System Demonstrations: 150–158, 2024. [原始来源](https://aclanthology.org/2024.eacl-demo.16/). DOI: 10.18653/v1/2024.eacl-demo.16.
