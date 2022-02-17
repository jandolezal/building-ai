"""
Exercise 18: TF-IDF

https://buildingai.elementsofai.com/Machine-Learning/working-with-text
"""


# Beginner
# What is the tf-idf score for word “Humpty” in line 4 of Humpty Dumpty?

import math

text = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.
'''
tf = 1/5
df = 3/4
tfidf = tf * math.log(1/df, 10)
print(round(tfidf, 2))


# Intermediate

# DATA BLOCK

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

import math

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            tfidf.append(tf[word][doc_index] * math.log(1/df[word], 10))
        print(tfidf)

main(text)
