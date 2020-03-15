# Work Plan

## Data Preparation

I need the following data before coding:

+ Employee Personal Information: done, provided by instructor
+ Tencent Word Embedding Datasets: done, download from: https://ai.tencent.com/ailab/nlp/embedding.html
+ Entity Lists
  + Chinese University List: done,download from: http://www.moe.gov.cn/jyb_xxgk/zdgk_sxml/sxml_gdjy/gdjy_gxsz/gxsz_xxmd/
  + Foreign University List (US, UK, etc): done

## Data Preprocess

+ Data input...

## Algorithm

### Word Segmentation

use jieba

### K-gram scan

do k-gram scan upon word list after word segmentation

### Entity Linking

compare word and entity in each list.

using cosine similarity



## Schedule

### stage1

1. 首先对文本进行预处理，包括【去除标点符号、去除stopwords，英文统一转为小写】
2. 写爬虫从各大网站抓取了学校、公司、企业职称、学位（只有三个，所以是直接写在代码里）组成知识库（entity list）
3. 然后是对知识库中的实体进行处理。找到知识库中的实体对应的embedding向量，如果不存在，则对该实体分词，该实体的embedding向量为组成该实体的每一个term的向量求和取平均。这里我的一个【创新点】是：对于像公司名这样的实体，分词后会存在大量譬如集团、有限公司等名称，而这些term并不能很好地去描述这个公司，所以我在求和的时候，为每一个term添加了权值，权值是该term在entity list中的IDF。这样如果这个词是比较有价值的，他的权值就会高。这个的效果体现在能过滤掉很多形如【公司->广州xx有限公司】这样的情况。这里的trick是对idf做了归一化，能够更大限度地区分term的价值。
4. 然后使用n-gram算法生成词块。demo中采用的是3，也就是把1-gram、2-gram、3-gram生成的所有词块作为待匹配的集合。然后遍历待匹配的集合，对于每一个词块，如果不存在向量就直接跳过（是一些无意义的词），否则，都与每个entity list中的实体对应的向量计算相似度（相似度的计算采用余弦），超过规定的阈值则认为链接成功。

目前遇到的问题：
1. 从匹配结果来看，许多的匹配都是完全匹配，embedding发挥的作用不是特别明显（学校名、学位名、职称基本都是完全匹配）。embedding能体现效果的地方有两个，一个是ceo->首席执行官，coo->首席运营官；另一个是爱国者->爱国者电子科技有限公司
2. 很多公司名字在embedding的模型中都无法找到对应的向量，指的是最关键信息的公司名字。
3. 如何对这个模型进行评价，衡量实验效果？我想到的有几个。一，信噪比。正确链接占返回结果的比重（precision）；二，能提取到的有用信息占所有有用信息的比重（recall）；三，设置对比试验。与精确匹配做比较。与不适用IDF作为权值做实验。

### 2020-02-19与老师交流

1. Metrics：人工标记出entity，然后求P@K，根据sim排序，前k个里面，有多少个是正确的。
2. 解决公司名匹配问题：公司名字可以采用正则匹配。如上海xxx有限公司，xxx不用匹配，知道是公司名就可以。
3. 结构化数据展示：【学校、学位】，【公司、职称】

### 2020-03-19与老师第二次交流

1. 添加时间：二元组->三元组
2. metrics：
   1. recall，在得出的结果中，有多少个是在groundtruth
   2. NDCG
   3. 排序：根据概率排序（有时间的、没时间的）
   4. 精确匹配
3. 可以开始论文写作

## Reference

1. [n-gram python](https://blog.csdn.net/MrLevo520/article/details/52149545)