from os import path
from wordcloud import (WordCloud, get_single_color_func)
import csv
import sys

class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping
       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.
       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)

d = path.dirname(__file__)

items_list = []

with open('items.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        items_list.append(row[1])

with open(sys.argv[1]) as f:
    content = f.readlines()
f.close()
visualize = open("visualize.txt", "w")
for item in content:
    row_list = item.split(',')
    if row_list[0].isdigit():
         length = len(row_list)
         for times in range(int(row_list[0])):
            for one_item in row_list[1:]:
                if one_item.isdigit():
                    visualize.write(items_list[int(one_item)-1])
            visualize.write("\n")
visualize.close()
text = open(path.join(d, 'visualize.txt')).read()

# Generate a word cloud image
wc = WordCloud(width = 1280, height = 720).generate(text)

grouped_color_func = SimpleGroupedColorFunc({}, 'white')
# Apply our color function
wc.recolor(color_func=grouped_color_func)

from PIL import Image
image = wc.to_image()
image.show()
image.resize((1280, 720))
image.save('wordcloud.jpg', format = "JPEG")
