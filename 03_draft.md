# 辞书知识与检索增强生成的融合：语义表示、技术路径与发展趋势

> 

## 摘要

数字技术使辞书由纸本文献转变为可检索资源，词汇语义研究进一步使义项、释义、例证及词汇关系成为可计算对象。大语言模型与检索增强生成的发展，为辞书知识参与问答、翻译、写作和语言教学提供了新的路径，也使信息来源、义项粒度和证据利用成为关键问题。本文采用主题式文献综述方法，围绕数字辞书与语义资源、释义和例句生成、文本及图结构检索、直接应用案例和评价方法梳理代表性工作。综述认为，辞书与RAG的融合不能简单理解为把辞书全文向量化后交给模型，而应建立从来源记录、义项识别、证据选择到答案生成的可追溯链条。现有研究已表明辞书信息可以在特定翻译及历史语言理解任务中提供有效支持，但跨语种、跨辞书和真实用户场景中的证据仍不充分。未来研究需要同时关注语义粒度、来源差异、按需检索、分层评价以及人工编纂责任，推动辞书从查询工具发展为可靠的语言知识服务基础。

**关键词：**数字辞书；词汇语义；义项对齐；检索增强生成；大语言模型；证据溯源

## 1 引言

辞书的数字化并不只是媒介替换。电子检索突破了纸本查阅的单一入口，使词形、释义、例证和关联信息可以通过不同路径访问。de Schryver较早系统讨论了电子辞书的形式、功能及其发展设想[1]。生成式人工智能出现后，研究问题进一步从“如何更快查到词条”转向“如何根据用户意图组织解释”。相关辞书学讨论已涉及释义撰写、例句生成以及编纂流程中的人机合作，但对自动生成能否满足辞书质量要求仍需谨慎判断[2]。

检索增强生成（retrieval-augmented generation，RAG）将外部检索知识与语言模型生成结合，为这一变化提供了技术条件[3]。对于辞书服务而言，潜在优势不仅是补充模型不知道的词，还在于使答案能够引用特定来源、呈现不同解释并控制适用语境。然而，“检索到了辞书”不代表“正确理解了辞书”。如果系统混淆同形词的不同义项，或者把多本辞书中不同粒度的解释合并成一个结论，检索也可能放大错误。多语言单语义项对齐研究已经把等价、宽泛、狭窄和相关等关系纳入标注，说明资源之间的对应并非简单的同义文本匹配[4]。

本文关注三个问题：辞书知识为什么需要与语义计算及RAG结合；不同技术分别解决了什么问题；现有证据允许我们对未来作出哪些判断。为避免对象混淆，本文将“使用模型辅助编纂辞书”与“使用辞书增强模型回答”分开讨论，将知识组织、表示学习和推理时检索视为可以组合、但不能相互替代的环节。本文的中心观点是：融合的重点应从增加可检索文本，转向构建可区分义项、可解释差异、可追踪来源的词汇证据体系。

### 1.1 综述范围与材料选择

本文属于主题式、批判性文献综述，而非穷尽检索的系统综述或元分析。文献以2020—2026年的相关研究为重点，回溯数字辞书和词汇语义资源的代表性基础工作。检索和核验主要利用ACL Anthology、NeurIPS与ICLR论文页、期刊出版页、作者机构页面及W3C社区报告，补充注明身份的arXiv预印本。围绕辞书、词汇语义、义项对齐、释义生成、dictionary-augmented prompting和RAG等主题组合检索。

本文将材料分为三类：直接利用辞书开展检索增强任务的研究；能够为辞书融合提供机制的相邻技术研究；数字辞书和语义资源的基础研究。只有第一类能够直接支持相应辞书应用的效果判断。正式论文、社区规范和预印本分别标明，不把软件说明或项目设想写成经过验证的学术结论。不同论文的语言、数据和指标并不一致，因此本文比较技术功能及证据边界，不制作跨任务的绝对性能排名。检索记录、阅读深度与参考文献对应关系另附于仓库，未声称所有文献均已全文精读。

## 2 从数字辞书到可计算的词汇知识

### 2.1 词汇语义资源提供了哪些结构？

传统释义适合人类阅读，但计算机要利用其中的关系，需要明确表示单位。WordNet通过同义词集及词汇语义关系组织英语词汇，为词义检索与语义关联提供了经典资源[5]。FrameNet以框架及框架元素连接词汇、语境和参与者结构，强调一个表达在何种情境中涉及哪些角色[6]。BabelNet则探索多语言词汇知识与百科知识的连接[7]。三者分别突出概念关联、框架结构和跨资源覆盖，不能仅因都具有“节点与边”就视作同一种辞书模型。

HowNet式资源从义原角度刻画词义构成。OpenHowNet开放了相应知识资源及访问工具，使细粒度语义知识更易被计算任务调用[8]。中文研究也探索了将义原表示与词向量学习结合，借助结构知识补充语料分布信息[9]。这一路线说明，辞书相关知识既可以被保存为外部可读结构，也可以参与模型训练。不过，义原标签、词性、框架角色和完整义项回答的是不同问题；将它们混成同一分类体系，会削弱表示的可解释性。

从上述工作可以概括出两类互补优势。显式语义资源能够标明关系类别并支持追溯，分布式表示则有利于发现表述不一致但语义接近的候选。前者的困难是构建和维护成本，后者的困难是相似度难以直接解释为明确关系。因而，辞书融合更合理的目标不是在符号与向量之间二选一，而是使两者分别承担候选发现、关系判断和证据组织等任务。

### 2.2 统一数据格式不等于统一意义

异构辞书的数字化还涉及编码层面的困难。TEI Lex-0旨在为机器可读辞书提供共同的基础编码方式，改善不同资源之间的互操作性[10]。OntoLex-Lemon则明确区分词条、词形、词汇义项与其语义引用，并采用通过引用关联词汇和本体对象的思路[11]。需要注意，后者是W3C社区组报告，而非W3C标准建议；其目标也不是给出覆盖一切自然语言的形式语义理论。

编码规范回答“信息存在哪里、字段如何连接”，义项对齐回答“两个来源描述的意义是什么关系”。二者不能互相代替。即使两部辞书都能输出相同JSON字段，其编号顺序、分义粒度和使用说明仍可能不同。Ahmadi等的对齐数据正表明，保留来源内部的义项身份，再判断来源间的关系，是可以独立开展的研究任务[4]。据此，本文认为，未来辞书RAG宜首先保留各来源的编号与原文，再建立可复核的映射，而不是在导入数据库时立即强制合并所有近似释义。

### 2.3 例证和语境不能退化为附属文本

辞书信息不仅包括定义，还包括说明实际用法的例句和书证。GDEX通过自动筛选语料中的适宜候选，辅助编纂者寻找好的辞书例句[12]。它体现的是从实际语言材料中选择证据，与模型凭提示新造例句属于不同过程。对知识库而言，这种区别关系到证据身份：语料例证可以说明实际出现过的用法，生成例句则首先是待检查的教学或解释材料。

WiC将同一个词在两个语境中是否同义作为评价目标，说明语义区分不一定要求模型输出一个统一义项编号[13]。但其二元判断也不能代替辞书间更细的宽窄和相关关系。综合来看，定义、例证与语境各有作用：定义概括意义，例证展示用法，关系标注说明二者如何对应。将它们混成没有类型区分的文本块，虽然便于一般检索，却不利于解释模型究竟使用了哪一种证据。

## 3 大语言模型如何改变辞书与语义研究

### 3.1 从生成释义到用释义表示意义

Noraset等的定义建模研究尝试从词向量生成自然语言释义，将词表示的内容通过可读文本表达出来[14]。另一方向是逆向词典：WantWords根据用户的描述寻找合适词语，支持中文、英文及跨语言查询[15]。前者由词到解释，后者由描述到词，两者都扩展了数字辞书的访问和表达方式，但并不因此自动构成RAG。

释义生成研究也逐渐从“能否写出一句解释”转向“解释是否在合适的语义粒度上”。Huang等专门讨论生成释义过于具体或过于宽泛的问题，并通过预训练模型与重排处理具体性[16]。Giulianelli等进一步把生成定义作为可解释的词义表示，用于语义变化分析[17]。这两项工作共同提示：自然语言释义不仅是最终输出，也可以是分析和比较意义的中间对象。由此出发，辞书RAG不能只追求回答更长、更丰富，还需防止在补充细节时改变原词义边界。

### 3.2 辞书编纂中的生成能力与质量责任

生成式模型能够为释义、例句和解释提供候选，但“候选产出”与“辞书编纂完成”之间仍有距离。de Schryver对早期ChatGPT辞书应用的讨论，体现了这一技术对编纂流程的冲击[2]。Cai等研究低成本辞书例句生成与评价，关注如何以自动方法提高候选选择效率[18]；方明炜等则从中文教学适用性出发，将规范性、语境独立性、典型度、词汇适切性及句法复杂度纳入评价[19]。它们共同说明，句子通顺只是质量要求的一部分。

对课程综述而言，评价这些工作需要避免两种极端：一是因为存在错误就否定所有生成辅助，二是因为若干示例优秀就认定编辑审核不再必要。中文教学例句可能语法成立，却不足以独立体现目标义项；一条综合释义可能内容合理，却未区分来源已经表达的信息和模型自行补充的信息。因此，生成技术更适合先承担候选建议、改写和辅助检查，再由明确的证据及质量程序约束其使用。

### 3.3 结构知识应当如何进入模型？

Meconi等对大语言模型词义理解进行系统评价，说明强模型在受测词义消歧和相关生成任务上已经具备相当能力[20]。因此，辞书知识增强不宜建立在“模型根本不懂词义”的简单假设上。更有价值的问题是：当来源之间存在细微差异、低频用法或复杂限制时，显式知识是否能改善判断及其可解释性。

SememeLRM提供了另一条答案。该工作先构造义原树，再用关系图编码与预训练语言模型结合，研究词汇关系分类和词汇蕴含[21]。这证明结构化词汇知识可以通过特定建模方式进入关系预测，但不是“将词典塞进提示词就提高生成质量”的证据。知识进入模型至少存在训练时融合、检索时使用和提示上下文序列化三种途径。它们对训练数据、模型参数访问、计算成本及迁移方式的要求不同，综述中必须据实际实验区分，而非统一冠以“语义增强”后直接比较。

## 4 辞书与RAG融合的技术路径

### 4.1 从文本检索到义项敏感的证据选择

RAG的基本链条是根据查询选择外部证据，再让生成模型利用这些证据作答。Lewis等的原始工作结合参数化生成模型与非参数化知识访问，并包含任务训练[3]。因此，RAG并不意味着绝不训练模型，也不意味着任何接入外部文档的系统都自动可靠。对辞书而言，实施之前首先要确定检索单位：整条词目、单个义项、定义片段和例证各自具有不同的信息密度及歧义风险。

稠密段落检索通过双编码器将查询与候选文本映射到表示空间，能处理部分字面不匹配的问题[22]。不过，语义相似的候选仍可能不符合当前词义、语体或年代。本文据此建议辞书场景结合词形和读音等精确线索、语义候选召回以及义项级重排。这里“义项级重排”的目的不是让文本看起来更相似，而是判断证据是否能支持当前问题。例如，查询某个词的古义时，仅因现代义解释更常见就优先返回它，并不能算成功检索。

在证据输入方面，完整词条适合回查来源，却不一定适合作为每次模型调用的固定上下文。一个义项只需要一段定义时，额外拼入大量兄弟义项可能增加混淆；反之，如果问题要求比较一个词的历时变化，只提供单一义项又会不足。因此，粒度应由问题决定，原始记录则保持可追溯。这个设计判断来自辞书对齐与检索机制的综合分析，仍需要具体辞书任务检验，不能当作已被通用RAG论文证明的结论。

### 4.2 按需检索：什么时候应该继续查？

一次检索不一定能提供完成复杂任务所需的全部信息。IRCoT使检索与中间推理交替进行，让已有信息影响后续查询[23]。Self-RAG通过学习反思标记，将检索需求与输出评价纳入生成过程[24]；Adaptive-RAG则训练较小的分类器，按问题复杂度选择不同检索策略[25]。三者都涉及适应性，但训练位置及控制方式不同，不能都描述为无需训练的提示方法。

对辞书服务，这些工作启发了一种问题驱动的展开方式：字音查询、释义解释、近义辨析和历史用法比较，不应机械地执行同一检索流程。若当前定义足以回答，应允许停止；若某个未明概念影响关系判断，再补充对应义项。停止规则还应考虑来源是否支持、是否出现冲突以及调用预算，而不只依赖模型自报的信心。这里的研究重点是取得足够而不过量的证据，不是让系统显示更多搜索步骤。

### 4.3 图结构检索不是一种统一的方法

Think-on-Graph让模型在知识图谱中探索实体与关系路径[26]。GraphRAG以实体图及社区摘要处理面向语料整体的综合问题，其初版发布于2024年，本文采用2025年的修订预印本[27]。HippoRAG则结合图结构与个性化PageRank实现关联检索[28]。这些工作提供了图导航、全局摘要和关联检索等不同机制，并不是同一类方法仅更换名称。

辞书语义图尤其需要保留词汇意义与百科实体的区别。一条“参见某词”的链接，可能帮助找到下一段解释，但并未证明两个义项等价；同一个字面词头，也可能对应不同读音或多个义项。若照搬实体图的统一节点方式，系统可能在建图阶段就抹平所要研究的语义差异。因此，图路线应将词形索引、来源义项和经核验的语义连接分开，而不能仅凭标签相同合并节点。

图越复杂也不必然越有价值。它会增加抽取、消歧、维护和证据选择的成本。对于已有足够明确信息的短定义，直接检索可能更合适；对于需要跨来源关联的任务，图结构才可能提供额外收益。本文因此倾向把文本与图看作可组合的工具，而不是“向量过时、图一定先进”的替代关系。

## 5 已有直接应用能支持什么结论？

### 5.1 低资源语言翻译：辞书条目作为外部知识

Merx等研究英语到Mambai语的低资源翻译，在提示中结合检索得到的平行句与相应辞书条目，并比较不同语言模型[29]。该研究与本文主题直接相关：辞书并非只供人查看，而是被整理为模型生成时可以调用的词汇证据。其结果支持在该语言和实验设置下使用词典信息，而不是仅依赖模型内部已经学到的知识。

这一案例的启示是，辞书增强未必需要先建立庞大语义图。将正确的词条与适合任务的例句送入模型，本身就有研究价值。其限制也清楚：翻译质量受到词形覆盖、词条粒度、平行句相关性和语言资源规模影响，局部改善不能自动推广为中文跨辞书义项比较的收益。后续研究应进一步区分词典内容本身与示例检索分别贡献了什么。

### 5.2 历史语言理解：证据需要匹配时间与查询意图

Eltanbouly和Rashwani以多哈阿拉伯语历史辞书为知识来源，构建混合检索、重排和意图路由管线，研究《古兰经》与圣训相关文本理解[30]。它把历时辞书知识引入RAG，说明语言理解中的外部知识不只涉及现实世界事实，也涉及词语在特定历史语境中的解释。该工作包含经过训练的组件，并结合模型裁判与人工核验，不能表述为无需训练、无需人工评价的通用方案。

本研究截至检索日按预印本引用，结论应限于其数据与评价条件。模型生成问题或自动评价可能带来与构建过程相关的偏差；扩大真实用户查询、不同体裁以及独立人工评价，是检验可迁移性的必要方向。对中文辞书研究，值得借鉴的是时间和问题意图参与检索，而不是把具体语言的实验得分直接作为预期效果。

### 5.3 两类技术证据不可混写

| 研究类别       | 代表工作                           | 已有证据支持的内容          | 不能直接推出的内容         |
| ---------- | ------------------------------ | ------------------ | ----------------- |
| 辞书支持翻译     | Mambai研究[29]                   | 特定低资源翻译中词条与例句检索的作用 | 所有中文词义任务均受益       |
| 历史辞书支持理解   | 多哈历史辞书RAG[30]                  | 特定历史阿拉伯语任务的辞书接入管线  | 跨语言、跨时期完全通用       |
| 结构知识支持关系预测 | SememeLRM[21]                  | 义原树与训练模型结合的词汇关系能力  | 同样结构直接提示LLM就有同等增益 |
| 通用检索控制与图方法 | IRCoT、ToG、GraphRAG[23][26][27] | 各自任务中的检索与证据组织机制    | 已经验证了汉语辞书专用方案     |

总体而言，直接辞书应用已经出现，但在本文选取的研究中，不同路线的语言、任务和资源条件差别显著。合理的综述结论不是“辞书RAG已经成熟”，也不是“尚无前人工作”，而是：若干直接案例提供了可行性证据，通用方法提供了可借鉴机制，二者之间还需要任务级的适配与独立验证。

## 6 评价、数据与应用中的主要问题

### 6.1 不能只评价答案是否流畅

辞书增强至少涉及三个评价层次。检索层要判断是否找到相关义项和充分证据；生成层要判断解释是否正确、粒度是否恰当；溯源层要判断引文是否真正支持相应断言。ALCE围绕带引用生成建立评价，提示回答内容与引用质量应分别检查[31]。RAGAs进一步区分检索上下文、回答忠实性和生成质量等因素[32]。这些框架能够提供工具，但自动裁判并不能替代所有辞书学判断。

对辞书任务，本文建议在通用指标之外增加义项混并、范围扩大或缩小、语体误用、例证错配与无依据补充等错误类别。举例说，假设两条说明分别写“常用于正式场合”和“仅用于正式场合”，生成答案不能把前者也解释成必要限制。这个例子是为说明评价维度而构造的，并非引自某部辞书。评测不仅要看最终句子像不像参考答案，还要确认程度词、否定和适用条件是否被忠实保留。

### 6.2 有证据不等于真正利用了证据

Liu等关于长上下文的信息利用研究表明，在其受测任务和模型中，相关信息所处位置会影响表现[33]。它提醒我们，增加上下文长度或拼入更多词典不自动带来更好的使用效果，但不应把该观察无条件外推到所有未来模型。对辞书系统，检索数量、证据排序及生成质量应当分别评价。

多跳也存在类似问题。MuSiQue强调步骤之间的真实信息依赖，防止所谓多跳问题通过单步捷径解决[34]。辞书图上的三条边，可能只是数据库引用跳转，而不是三步推理。较有说服力的评价应标出至少一种充分证据集合，并通过移除关键支持、替换同词异义节点或改变证据顺序，观察模型判断是否相应变化。如果结论完全不依赖所检索资料，就不能仅凭显示了路径而宣称系统完成了证据推理。

### 6.3 人工一致性与语义歧义

多来源辞书未必对同一词作出完全一致的分类，不同编纂目标也可能导致合理差异。因此，建立评测数据时要允许“证据不足”或“边界有争议”，而不将所有分歧自动当作噪声。Artstein和Poesio指出，标注一致性的计算应与任务尺度及统计假设匹配[35]。据此，义项关系、文本片段和来源核验不宜只用同一个总分评价。

人工关系标签还应尽量独立于待验证的中间表示。如果研究者先规定某种结构组合必定对应某个标签，再用同一规则生成答案，就难以判断模型是否真正改善了语义理解。数据划分也需警惕同一词、近重复来源和同底本材料跨集合出现。以上属于本文对评测设计的归纳建议，不能写成某一现成数据集已完全解决的事项。

### 6.4 来源质量、可复现性与使用权限

辞书作为相对经过编纂的资源，并不意味着所有电子版本都无误。编码转换、词条截断、分义标记和来源身份会影响可检索证据。TEI Lex-0与OntoLex-Lemon提供的互操作思想有助于组织信息，但具体项目仍需保留原文、转换记录和来源定位[10][11]。因此，数据清洗必须区别机械错误与真实语义差异，不能为了统一格式顺便把不同释义改写成相同表述。

复现与公开还涉及来源使用条件。能够在线阅读、能够购买数字版、能够批量处理及能够再次公开分发，是不同层面的权限问题。本文不作特定司法辖区的法律结论，而建议逐来源记录适用条款，并将原始文本、派生标注和实验代码分开管理。模型生成的释义和例句也应保留其生成身份，不应伪装为辞书原文。技术上的可下载和可复制，不等于已经完成合法来源及发布范围核验。

## 7 发展方向：从词条检索到可追溯的语义服务

### 7.1 以来源义项而非无差别文本块组织证据

由义项对齐和词汇链接模型可以提出一个方向：保留各辞书内部的义项与编号，将跨来源关系作为单独可修订的层次[4][11]。这既方便检索，也能够解释某个结论是来源共识、相互补充还是存在差异。对用户而言，答案不必强行把多种说法融成一个看似统一的定义；在必要时呈现差异及对应证据，可能比消除分歧更有帮助。这里的“可能”需要用户任务和实验支持，而非先验优越性。

### 7.2 用轻量结构帮助检索，但不追求无限分解

WordNet、框架语义和义原资源已经提供不同层面的结构知识。未来可探索将适合当前问题的少量结构作为模型外部上下文，用于定位待解释成分和选择证据。这不意味着结构序列化本身是新发明，也不意味着可以省略消歧。需要比较它相对于原始定义、普通文字摘要和其他结构化表示是否提供额外信息。

相应地，按需检索宜围绕具体信息缺口，而不是以“可达节点全部展开”为目标。选择多少节点、哪些关系可以沿用、何时停止，应与任务收益和成本一起评估。模型自反思、问题复杂度路由及图探索提供了不同控制机制[24][25][26]；辞书研究的贡献可以落在其语义条件与证据要求的具体化，而不是仅给已有机制更换名称。

### 7.3 将“生成候选”和“验证解释”纳入同一流程

释义与例句生成研究显示，语言模型能够承担多种辞书相关任务，而具体性、典型性和教学适切性又需要专门评价[16][18][19]。未来系统可使候选生成、来源检索、证据核验和人工修订形成连续流程。对于写作服务，系统应帮助用户辨析表达；对于语言教学，应考虑学习者水平；对于历史文本，应提供与时期相符的词义证据。不同需求应共享可追溯基础，而不是接受完全相同的生成答案。

### 7.4 建立多语言、跨来源、可审计的评价体系

现有直接应用案例提示，辞书增强的价值可能与语言资源稀缺程度、查询类型和时间信息密切相关[29][30]。后续研究应覆盖不同语种与辞书类型，报告未见词、未见来源及真实用户问题上的表现，同时明确数据和模型版本。评价宜兼顾准确性、证据充分性、引用可靠性、响应时间与维护成本；涉及人工判断时报告标注程序和一致性，而非只列一个综合分数[31][32][35]。

综上，未来方向不是让辞书全面替代模型知识，也不是让模型消解辞书编辑责任，而是确定二者在何种条件下互相补足：辞书提供有来源的词汇解释，模型提供自然语言交互和信息组织能力，结构及评价机制则约束二者如何连接。

## 8 结语

辞书、词汇语义与RAG的发展呈现的是多条研究路线逐步汇合，而非新技术对旧技术的简单替代。数字辞书改善访问与编码，词汇语义资源明确可计算关系，生成模型扩展解释和例句生产，RAG则把外部证据引入回答过程。各环节分别解决一部分问题，也各有边界。

本文所梳理的研究支持一个审慎结论：辞书知识已在部分检索增强应用中显示价值，但可靠的融合仍取决于义项粒度、来源保留、证据选择和分层评价。后续工作应在具体任务中验证结构与检索是否真正改善语义判断，避免以更多节点、更长上下文或更流畅的答案代替可靠性。对辞书学和语言技术而言，值得追求的共同目标是让解释既易于使用，也能够说明其来源、适用条件与不确定性。

## 参考文献

[1] DE SCHRYVER G M. Lexicographers’ Dreams in the Electronic-Dictionary Age[J]. International Journal of Lexicography, 16(2): 143–199, 2003. [原始来源](https://doi.org/10.1093/ijl/16.2.143). DOI: 10.1093/ijl/16.2.143.

[2] DE SCHRYVER G M. Generative AI and Lexicography: The Current State of the Art Using ChatGPT[J]. International Journal of Lexicography, 36(4): 355–387, 2023. [原始来源](https://doi.org/10.1093/ijl/ecad021). DOI: 10.1093/ijl/ecad021.

[3] LEWIS P, PEREZ E, PIKTUS A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks[C]. Advances in Neural Information Processing Systems, 33, 2020. [原始来源](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html).

[4] AHMADI S, MCCRAE J P, NIMB S, et al. A Multilingual Evaluation Dataset for Monolingual Word Sense Alignment[C]. Proceedings of LREC 2020: 3232–3242, 2020. [原始来源](https://aclanthology.org/2020.lrec-1.395/).

[5] MILLER G A. WordNet: A Lexical Database for English[J]. Communications of the ACM, 38(11): 39–41, 1995. [原始来源](https://doi.org/10.1145/219717.219748). DOI: 10.1145/219717.219748.

[6] BAKER C F, FILLMORE C J, LOWE J B. The Berkeley FrameNet Project[C]. 36th Annual Meeting of the ACL and 17th International Conference on Computational Linguistics, Volume 1: 86–90, 1998. [原始来源](https://aclanthology.org/P98-1013/). DOI: 10.3115/980845.980860.

[7] NAVIGLI R, PONZETTO S P. BabelNet: Building a Very Large Multilingual Semantic Network[C]. Proceedings of ACL 2010: 216–225, 2010. [原始来源](https://aclanthology.org/P10-1023/).

[8] QI F, YANG C, LIU Z, et al. OpenHowNet: An Open Sememe-based Lexical Knowledge Base[EB/OL]. arXiv:1901.09957, 2019. [原始来源](https://arxiv.org/abs/1901.09957). DOI: 10.48550/arXiv.1901.09957.

[9] 于宁, 王江萍, 石宇, 等. 基于义原表示学习的词向量表示方法[C]. 第二十届中国计算语言学大会论文集: 57–65, 2021. [原始来源](https://aclanthology.org/2021.ccl-1.6/).

[10] TASOVAC T, ROMARY L, SALGADO A. TEI Lex-0: A baseline encoding for lexicographic data[R/OL]. ELEXIS – European Lexicographic Infrastructure, 2018. [原始来源](https://novaresearch.unl.pt/en/publications/tei-lex-0-a-baseline-encoding-for-lexicographic-data/).

[11] CIMIANO P, MCCRAE J P, BUITELAAR P, eds. Lexicon Model for Ontologies: Community Report, 10 May 2016[R/OL]. W3C Ontology-Lexicon Community Group, 2016. [原始来源](https://www.w3.org/2016/05/ontolex/).

[12] KILGARRIFF A, HUSÁK M, MCADAM K, et al. GDEX: Automatically Finding Good Dictionary Examples in a Corpus[C]. Proceedings of the 13th EURALEX International Congress: 425–432, 2008. [原始来源](https://euralex.org/publications/gdex-automatically-finding-good-dictionary-examples-in-a-corpus/).

[13] PILEHVAR M T, CAMACHO-COLLADOS J. WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations[C]. Proceedings of NAACL-HLT 2019, Volume 1: 1267–1273, 2019. [原始来源](https://aclanthology.org/N19-1128/). DOI: 10.18653/v1/N19-1128.

[14] NORASET T, LIANG C, BIRNBAUM L, et al. Definition Modeling: Learning to Define Word Embeddings in Natural Language[C]. Proceedings of the AAAI Conference on Artificial Intelligence, 31(1), 2017. [原始来源](https://ojs.aaai.org/index.php/AAAI/article/view/10996). DOI: 10.1609/aaai.v31i1.10996.

[15] QI F, ZHANG L, YANG Y, et al. WantWords: An Open-source Online Reverse Dictionary System[C]. Proceedings of EMNLP 2020: System Demonstrations: 175–181, 2020. [原始来源](https://aclanthology.org/2020.emnlp-demos.23/). DOI: 10.18653/v1/2020.emnlp-demos.23.

[16] HUANG H, KAJIWARA T, ARASE Y. Definition Modelling for Appropriate Specificity[C]. Proceedings of EMNLP 2021: 2499–2509, 2021. [原始来源](https://aclanthology.org/2021.emnlp-main.194/). DOI: 10.18653/v1/2021.emnlp-main.194.

[17] GIULIANELLI M, LUDEN I, FERNÁNDEZ R, et al. Interpretable Word Sense Representations via Definition Generation: The Case of Semantic Change Analysis[C]. Proceedings of ACL 2023, Volume 1: 3130–3148, 2023. [原始来源](https://aclanthology.org/2023.acl-long.176/). DOI: 10.18653/v1/2023.acl-long.176.

[18] CAI B, CLARENCE N, LIANG D, et al. Low-Cost Generation and Evaluation of Dictionary Example Sentences[C]. Proceedings of NAACL-HLT 2024, Volume 1: 3538–3549, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.194/). DOI: 10.18653/v1/2024.naacl-long.194.

[19] 方明炜, 朱君辉, 鲁鹿鸣, 等. 例句质量评估体系构建及大语言模型例句生成能力评估[C]. 第二十四届中国计算语言学大会论文集: 117–130, 2025. [原始来源](https://aclanthology.org/2025.ccl-1.10/).

[20] MECONI D, STIRPE S, MARTELLI F, et al. Do Large Language Models Understand Word Senses?[C]. Proceedings of EMNLP 2025: 33897–33916, 2025. [原始来源](https://aclanthology.org/2025.emnlp-main.1720/). DOI: 10.18653/v1/2025.emnlp-main.1720.

[21] WANG H, LIANG Q, WANG Y, et al. Enhancing Lexical Relation Mining with Structured Sememe Knowledge[C]. Proceedings of ACL 2026, Volume 1: 4930–4947, 2026. [原始来源](https://aclanthology.org/2026.acl-long.224/). DOI: 10.18653/v1/2026.acl-long.224.

[22] KARPUKHIN V, OGUZ B, MIN S, et al. Dense Passage Retrieval for Open-Domain Question Answering[C]. Proceedings of EMNLP 2020: 6769–6781, 2020. [原始来源](https://aclanthology.org/2020.emnlp-main.550/). DOI: 10.18653/v1/2020.emnlp-main.550.

[23] TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions[C]. Proceedings of ACL 2023, Volume 1: 10014–10037, 2023. [原始来源](https://aclanthology.org/2023.acl-long.557/). DOI: 10.18653/v1/2023.acl-long.557.

[24] ASAI A, WU Z, WANG Y, et al. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html).

[25] JEONG S, BAEK J, CHO S, et al. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity[C]. Proceedings of NAACL-HLT 2024, Volume 1: 7036–7050, 2024. [原始来源](https://aclanthology.org/2024.naacl-long.389/). DOI: 10.18653/v1/2024.naacl-long.389.

[26] SUN J, XU C, TANG L, et al. Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph[C]. The Twelfth International Conference on Learning Representations, 2024. [原始来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html).

[27] EDGE D, TRINH H, CHENG N, et al. From Local to Global: A Graph RAG Approach to Query-Focused Summarization[EB/OL]. arXiv:2404.16130v2（初版2024；本清单采用2025修订版）, 2025. [原始来源](https://arxiv.org/abs/2404.16130v2). DOI: 10.48550/arXiv.2404.16130.

[28] JIMÉNEZ GUTIÉRREZ B, SHU Y, GU Y, et al. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models[C]. Advances in Neural Information Processing Systems, 37, 2024. [原始来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6ddc001d07ca4f319af96a3024f6dbd1-Abstract.html).

[29] MERX R, MAHMUDI A, LANGFORD K, et al. Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language[C]. Proceedings of the 2nd EURALI Workshop @ LREC-COLING 2024: 1–11, 2024. [原始来源](https://aclanthology.org/2024.eurali-1.1/).

[30] ELTANBOULY S, RASHWANI S. Grounding Arabic LLMs in the Doha Historical Dictionary: Retrieval-Augmented Understanding of Quran and Hadith[EB/OL]. arXiv:2603.23972v1, 2026. [原始来源](https://arxiv.org/abs/2603.23972). DOI: 10.48550/arXiv.2603.23972.

[31] GAO T, YEN H, YU J, et al. Enabling Large Language Models to Generate Text with Citations[C]. Proceedings of EMNLP 2023: 6465–6488, 2023. [原始来源](https://aclanthology.org/2023.emnlp-main.398/). DOI: 10.18653/v1/2023.emnlp-main.398.

[32] ES S, JAMES J, ESPINOSA ANKE L, et al. RAGAs: Automated Evaluation of Retrieval Augmented Generation[C]. Proceedings of EACL 2024: System Demonstrations: 150–158, 2024. [原始来源](https://aclanthology.org/2024.eacl-demo.16/). DOI: 10.18653/v1/2024.eacl-demo.16.

[33] LIU N F, LIN K, HEWITT J, et al. Lost in the Middle: How Language Models Use Long Contexts[J]. Transactions of the Association for Computational Linguistics, 12: 157–173, 2024. [原始来源](https://aclanthology.org/2024.tacl-1.9/). DOI: 10.1162/tacl_a_00638.

[34] TRIVEDI H, BALASUBRAMANIAN N, KHOT T, et al. ♫ MuSiQue: Multihop Questions via Single-hop Question Composition[J]. Transactions of the Association for Computational Linguistics, 10: 539–554, 2022. [原始来源](https://aclanthology.org/2022.tacl-1.31/). DOI: 10.1162/tacl_a_00475.

[35] ARTSTEIN R, POESIO M. Survey Article: Inter-Coder Agreement for Computational Linguistics[J]. Computational Linguistics, 34(4): 555–596, 2008. [原始来源](https://aclanthology.org/J08-4004/). DOI: 10.1162/coli.07-034-R2.
