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


# Advanced

import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


# Two functions used in exercise 17 Bag of words
def distance(row1, row2):
    # It seems exercise tests want Euclidian distance
    return math.sqrt(sum((count1 - count2)**2 for count1, count2 in zip(row1, row2)))

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i, row1 in enumerate(data):
        for j, row2 in enumerate(data):
            if i == j:
                dist[i, j] = np.Inf
            else:
                dist[i, j] = distance(row1, row2)
    return np.unravel_index(np.argmin(dist), dist.shape)


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]

    docs = [line.lower().split() for line in text.split('\n')]
    unique_words = list(set(word for sentence in docs for word in sentence))

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    
    # It seems that there tf and tfidf should be computet also for words which are not in the document (line)
    # https://spectrum.chat/elementsofai/buildingai/exercise-18-tf-idf-advanced-help-needed~a9e1d6ca-fe43-4c91-bbd3-270956c0971b
    
    tfs = []

    for doc in docs:
        tfs.append([doc.count(unique_word)/len(doc) if unique_word in doc else 0 for unique_word in unique_words])
    
    dfs = {}
    for word in unique_words:
        dfs[word] = sum(word in doc for doc in docs)/len(docs)
    
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    tfidfs = []

    for row in tfs:
        tfidfs.append([tf * math.log(1/dfs[unique_words[i]], 10) for i, tf in enumerate(row)])

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    # Tests are checking printed values, not returned!
    print(find_nearest_pair(tfidfs))


main(text)

