# coding:utf-8
import time, os
import numpy as np
import pandas as pd

def tf(word, count):
    return count[word] / sum(count.values())

def idf(word, count_list):
    word_in_doc_sum = sum(1 for count in count_list if word in count)
    return np.log( len(count_list) / (1 + word_in_doc_sum) )

def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)

def tfidf_transform():
    pass
