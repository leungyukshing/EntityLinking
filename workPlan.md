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

## Reference

1. [n-gram python](https://blog.csdn.net/MrLevo520/article/details/52149545)