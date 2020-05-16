# encoding=gbk
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

lyric = ''
f = open("things.txt", "r", encoding='UTF-8')
for i in f:
    lyric += f.read()

result = jieba.analyse.textrank(lyric, topK=50, withWeight=True)
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)

image = Image.open('../static/tim.jpg')
graph = np.array(image)
wc = WordCloud(font_path='./fonts/simhei.ttf', background_color='White', max_words=50, mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
# plt.show()
# wc.to_file('dream.png')
