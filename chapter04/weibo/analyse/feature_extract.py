# coding:utf-8
import time, os
from collections import Counter

import jieba

STOP_WORDS = set()

def set_stop_words(stop_words_path):
    global STOP_WORDS

    abs_path = os.path.normpath( os.path.join( os.getcwd(), stop_words_path )  )
    if not os.path.exists(abs_path):
        raise Exception("stop words path does not exist:" + abs_path)
    content = open(abs_path,'rb').read().decode('utf-8')
    lines = content.split('\n')
    for line in lines:
        STOP_WORDS.add(line)
    #return

def extract_words(sentence):
    global STOP_WORDS

    words = jieba.cut(sentence, cut_all=True)
    word_count = Counter(words)
    freq = {}
    for w, count in word_count.items():
        if len(w.strip())<2: continue
        if w.lower() in STOP_WORDS: continue
        freq[w.lower()] = count

    return freq
    # return list(freq.items())

