from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest
import sys

def open_Document(filename):
    with open(filename, 'r') as fp:
        text = fp.read()
    return text


def get_tokenize(text):
    return word_tokenize(text), sent_tokenize(text)


def get_stops(words):
    stopw = set(stopwords.words('portuguese') + list(punctuation))
    no_stopw = [word for word in words if word not in stopw]
    return stopw, no_stopw


def sentences(sent, freq):
    usable_sents = defaultdict(int)
    for i, sentence in enumerate(sent):
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                usable_sents[i] += freq[word]
    return usable_sents


def resumer(u_sents, num, sent):
    index_sents = nlargest(num, u_sents, u_sents.get)
    summary = ''
    for i in sorted(index_sents):
        summary += sent[i]
    return summary


def main(argv):
    text = open_Document(argv [1])
    words, sents = get_tokenize(text)
    stopw, nostopw = get_stops(words)
    freq = FreqDist(nostopw)
    u_sents = sentences(sents, freq)
    summary = resumer(u_sents, int(argv[2]), sents)
    print(summary)

if __name__ == '__main__':
    main(sys.argv)