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

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


# text = '''he really really loves coffee
# my sister dislikes coffee
# my sister loves tea'''


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + abs(ai - bi)
    return sum


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]

    docs = [line.lower().split() for line in text.split('\n')]
    words = list(set(word for sentence in docs for word in sentence))

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    tfs = []
    for doc in docs:
        tfs.append({word: doc.count(word)/len(doc) for word in set(doc)})
    dfs = {}
    for word in words:
        dfs[word] = sum(word in doc for doc in docs)/len(docs)
    
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    tfidfs = []
    for i, doc in enumerate(docs):
        tfidfs.append([tfs[i][word] * math.log(1/dfs[word], 10) for word in set(doc)])

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    distances = {}

    for i, line1 in enumerate(tfidfs):
        for j, line2 in enumerate(tfidfs):
            if i == j:
                continue
            else:
                distances[(i, j)] = dist(line1, line2)

    sorted_distances = [k for k, v in sorted(distances.items(), key=lambda item: item[1])]

    return sorted_distances[0]

print(main(text))
