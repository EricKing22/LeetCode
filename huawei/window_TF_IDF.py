import math
import numpy as np


N = int(input())
corpus = []
for _ in range(N):
    corpus.append(input().split())

K = int(input())
P = int(input())

querys = []
for _ in range(P):
    x = list(input().split())
    t = x[0]
    q = x[1:]
    querys.append((int(t),q))

def TF(word, doc):
    dos_length = len(doc)
    word_frequency = 0
    for w in doc:
        if w == word:
            word_frequency += 1
    return word_frequency / dos_length


def IDF(corpus, word):
    N = len(corpus)
    M = sum([1 if word in doc else 0 for doc in corpus])
    return math.log( (N+1) / (M + 1)) + 1

As = []
Bs = []
for query in querys:
    t, q = query
    docs_in_window = corpus[max(0,t-K) : t+1]

    A = []
    for word in q:
        tf = TF(word, q)
        idf = IDF(docs_in_window, word)
        A.append(tf * idf)
    As.append(A)

    B_query = []
    for (j,doc) in enumerate(docs_in_window):
        B = []
        weight = (j+1) / K
        for word in q:
            tf = TF(word, doc)
            idf = IDF(docs_in_window, word)

            B.append(tf * idf * weight)
        B_query.append(B)

    Bs.append(B_query)


def cos(A,B):
    A = np.array(A)
    B = np.array(B)
    dot = np.dot(A, B)
    if dot == 0:
        return 0

    return dot / (np.linalg.norm(A) * np.linalg.norm(B))

ans = []

for (A,query) in zip(As, querys):
    t = query[0]
    max_sim = 0
    result = -1

    B_query = Bs.pop(0)
    for (i,B) in enumerate(B_query):
        if max_sim < cos(A, B) and cos(A,B) >= 0.6:
            max_sim = cos(A,B)
            result = int(max(0,t - K) + i)
            break

    ans.append(str(result))

print(" ".join(ans))

