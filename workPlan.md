# Work Plan

## Data Preparation

I need the following data before coding:

+ Employee Personal Information: done, provided by instructor
+ Tencent Word Embedding Datasets
+ Entity Lists
  + Chinese University List: done,download fromhttp://www.moe.gov.cn/jyb_xxgk/zdgk_sxml/sxml_gdjy/gdjy_gxsz/gxsz_xxmd/
  + Foreign University List (US, UK, etc)



## Algorithm

### Word Segmentation

use jieba

### K-gram scan

do k-gram scan upon word list after word segmentation

### Entity Linking

compare word and entity in each list.