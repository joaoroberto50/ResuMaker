from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest


def _get_tokenize(text):
    return word_tokenize(text), sent_tokenize(text)


def _get_stops(words):
    stopw = set(stopwords.words('portuguese') + list(punctuation))
    no_stopw = [word for word in words if word not in stopw]
    return stopw, no_stopw


def _sentences(sent, freq):
    usable_sents = defaultdict(int)
    for i, sentence in enumerate(sent):
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                usable_sents[i] += freq[word]
    return usable_sents


def _get_resumer(u_sents, num, sent):
    index_sents = nlargest(num, u_sents, u_sents.get)
    summary = ''
    for i in sorted(index_sents):
        summary += sent[i]
    return summary


def resumer(text, n_sent):
    words, sents = _get_tokenize(text)
    stopw, nostopw = _get_stops(words)
    freq = FreqDist(nostopw)
    u_sents = _sentences(sents, freq)
    summary = _get_resumer(u_sents, int(n_sent), sents)
    return summary

