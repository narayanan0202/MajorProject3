import nltk
import numpy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag, pprint
text = "hello world this is a simple test. Mr. Jack and Jill went up the hill"

sents=sent_tokenize(text)

print(sents)

words = word_tokenize(text)
print(words)

print(nltk.wordpunct_tokenize(text))
print(nltk.pos_tag(words))

def entities(text):
    return ne_chunk(
        pos_tag(
            word_tokenize(text)))


tree = entities("Standing in the doorway of a Boeing 747, former president Barack Obama has one arm wrapped. ")
tree.pprint()
#tree.draw()
print("This is the last feature to test on github for now")

#The changes i am making now to test github..... let see how it works