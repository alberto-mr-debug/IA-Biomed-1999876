#link TO COLLAB: https://colab.research.google.com/drive/1N8Wc0s1WvNNqC70g979YBOgEDo9tralo?usp=sharing

import re #this library over here will help us by counting the sentences in the text
from collections import Counter
text = """he will win who knows when to figth and when not to figth.
          he will win who knows how to handle both superior and inferior
          forces. Move swift as the wind and closely formed as the wood.

          
          Atack like the fire and be still as the mountain. SUN TZU
          ART OF WAR."""
words = text.split()# the split (), i used the blank space
# between each word to separete them all

sentences = re.split(r'(?<=[.!?])', text.strip())#now here we are sayig that all sentences
#can be separeted by this types of symbols
sentences_count= len([s for s in sentences if s.strip()])

paragraphs = text.strip().split('\n\n')#this is for separete the paragraphs

paragraph_count = len([p for p in paragraphs if p.strip()])#here we count how many paragraphs exist

T=text.lower()
P = re.findall(r'\b\w+\b', T)

word_counts = Counter(P)
most_common_words = word_counts.most_common(5)
#printing zone
print("the total words are: ",len(words))
print(f'Total number of sentences: {sentences_count}')
print(f'Total number of paragraphs: {paragraph_count}')
print("Most common words and their frequencies:")
for P, frequency in most_common_words:
    print(f'{P}: {frequency}')