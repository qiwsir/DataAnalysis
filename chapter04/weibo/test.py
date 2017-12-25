import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
from wordcloud import WordCloud

import jieba

STOP_WORDS = set()

app_path = os.path.dirname( os.path.dirname(__file__) )

stop_words_txt = os.path.join(app_path, 'stopwords.txt')

with open(stop_words_txt) as f:
    for line in f:
        STOP_WORDS.add(line[:-1])


file = './weibo_data.csv'
weibo_datas = pd.read_csv(file)

content_weibo = weibo_datas['weibo_cont']
content_weibo_cut = content_weibo.apply(jieba.cut)

import re

def filter_words(words, stop_words):
    result = [w for w in words if w not in stop_words and len(w)>1 and re.match("^[\u4e00-\u9fa5]{0,}$", w)]
    return result


word_freq = dict()

for one in content_weibo_cut:
    row = filter_words(list(one), STOP_WORDS)
    if row:
        for word in row:
            word_freq[word] = word_freq.get(word, 0) + 1

# from scipy.misc import imread

#app_path = os.path.dirname( os.path.dirname(__file__) )

# back_image = imread(os.path.join(app_path, 'back.png'))
font_path = os.path.join(app_path, 'simkai.ttf')

word_cloud = WordCloud(font_path=font_path,  # 设置字体
                   background_color="white",  # 背景颜色
                   max_words=200,  # 词云显示的最大词数
                   #mask=back_image,  # 设置背景图片
                   max_font_size=100,  # 字体最大值
                   random_state=42,
                   width=600, height=400, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
        )
word_cloud.generate_from_frequencies(word_freq)
#image_colors = ImageColorGenerator(back_image)

plt.figure()
plt.imshow(word_cloud)
plt.axis("off")

plt.show()
