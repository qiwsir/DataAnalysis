# coding:utf-8
import time, os

from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

app_path = os.path.dirname( os.path.dirname(__file__) )

#back_coloring_path = os.path.join(app_path, 'imgs/1.jpeg')
font_path = os.path.join(app_path, 'fonts/simkai.ttf')


def get_word_cloud(word_freq, file_path):
#    back_coloring = imread(back_coloring_path)# 设置背景图片
    wc = WordCloud(font_path=font_path,  # 设置字体
                   background_color="white",  # 背景颜色
                   max_words=200,  # 词云显示的最大词数
                   #mask=back_coloring,  # 设置背景图片
                   max_font_size=100,  # 字体最大值
                   random_state=42,
                   width=600, height=400, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
        )

    wc.generate_from_frequencies(word_freq)
   # image_colors = ImageColorGenerator(back_coloring)

    plt.figure()
    plt.imshow(wc)
    plt.axis("off")

    # plt.figure()
    # plt.imshow(wc.recolor(color_func=image_colors))
    # plt.axis("off")

    plt.show()

    # 保存图片
    # wc.to_file(file_path)
