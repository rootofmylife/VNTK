# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import PlaintextCorpusReader
from vntk import vntk, Corpus

# text = vntk('./')

# corpus = vntk.open_corpus('./corpus.txt')

# corpus = Corpus(corpus)
# corpus.concordance('những')


# mess = open('./data_corpus.txt', 'r', encoding='utf-8').read()

# extract key words and phrases that sum up the style and content of a text
# token = nltk.word_tokenize(mess)
# corpus = nltk.Text(token)

'''
Chapter 1
'''
# print(corpus.concordance('hóa')) # tìm những khúc chứa những từ này
# print(corpus.similar('ngâm')) # tìm những câu có cùng ngữ cảnh với từ này, giống y hệt
# print(corpus.common_contexts(['ngâm', 'đau'])) # examine just the contexts that are shared by two or more words
# print(corpus.generate(words=None)) # có thể đã bị xóa bởi nhân viên, https://github.com/nltk/nltk/issues/736
# print(corpus.dispersion_plot(['ngâm', 'tạo', 'phẩm'])) # xác định vị trí mỗi từ, bắt đầu từ đầu của corpus
# print(len(set(corpus))) # đếm token trong corpus
# print(corpus.count('ngâm')) # đếm số lần xuất hiện

# fdist = nltk.FreqDist(corpus)
# nltk.FreqDist(corpus).max() # tìm ra từ xuất hiện nhiều nhất
# print(fdist) # số lượng từ vựng chưa bỏ trùng
# print(fdist.keys()) # in ra bộ từ vựng
# print(fdist['ngâm']) # lấy ra tần số suất hiện của từ này
# fdist.plot(50, cumulative=True) # graph về tần số của 50 từ đầu tiên
# print(fdist.hapaxes()) # in ra những từ xuất hiện 1 lần
# fdist.freq('monstrous') # Frequency of a given sample
# fdist.N() # Total number of samples
# for sample in fdist: # Iterate over the samples, in order of decreasing frequency
# fdist.max() # Sample with the greatest count
# fdist.tabulate() # Tabulate the frequency distribution
# find bigrams that occur more often than we would expect based on the frequency of individual words
# print(corpus.collocations()) # tìm ra các cặp câu, mà có số lần xuất hiện nhiều hơn 1 từ trong câu đó

'''
Chapter 2
'''
# wordlists = PlaintextCorpusReader('./', '.*')
# for (fileid, value) in enumerate(wordlists.fileids()): # fileids([categories])
#    print('text' + str(fileid) + ': ' + str(value))
# print(wordlists.sents('corpus.txt')) # raw(), words(), sents()
# nltk.ConditionalFreqDist(condition, event)

# Generating Random Text with Bigrams

# sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven']
# for i in nltk.bigrams(sent):
#     print(i)


# def generate_model(cfdist, word, num=15):
#     for it in range(num):
#         print(word)
#         word = cfdist[word].max()

# big = nltk.bigrams(token)
# cfd = nltk.ConditionalFreqDist(big)
# print(generate_model(cfd, 'chính'))

'''
Chapter 5
'''

# text = nltk.word_tokenize("tôi ăn cơm")
# print(nltk.pos_tag(text)) # đánh dấu POS

# tagged_token = nltk.tag.str2tuple('đứng_lên/VP') # tách các từ dc đánh dấu ra
# print(tagged_token)

#  nltk.corpus.vietnam.tagged_words() = > [(đứng_lên, 'VP'), ()] # đưa ra các từ dc đánh dấu

# print(sorted(set(b for (a, b) in nltk.bigrams(corpus) if a == 'ngâm'))) # xuất ra bi-gram có từ a đứng trc

# chỉ dùng cho câu
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1 + ' ' + w2 + ' ' + w3)

# xuất ra những từ có nhiều POS
'''
vn_news_tagged = vn.tagged_words(categories='news')
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)

for word in data.conditions():
    if len(data[word]) > 3:
        tags = data[word].keys()
        print(word + ' '.join(tags))

'''
#  Program to find the most frequent noun tags.
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

# tagdict = findtags('NN', nltk.corpus.vn.tagged_words(categories='news'))
# for tag in sorted(tagdict):
#    print(tag + ' ' + tagdict[tag])

# the most common verbs in news text
'''
wsj = nltk.corpus.vn.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(wsj)
print( [word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')])
'''

# Đếm số lượng từ được sử dụng
'''
counts = nltk.defaultdict(int)
for (word, tag) in nltk.corpus.vn.tagged_words(categories='news'):
    counts[tag] += 1
'''

# Traing N-gram for POS
# raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
# tokens = nltk.word_tokenize(raw)
# default_tagger = nltk.DefaultTagger('NN')
# print(default_tagger.tag(tokens))

# convert utf-16 -> utf-8
# wordlists = PlaintextCorpusReader('./data/VTB/', '.*')
# for (fileid, value) in enumerate(wordlists.fileids()):
#     file_input = open('./data/VTB/' + value, 'r', encoding='utf-16').read()
#     name = value.split('/')[1]
#     file_output = open('./VTB_utf8/' + name, 'w', encoding='utf-8')
#     file_output.write(file_input)
#     file_output.close()

'''
wordlists = PlaintextCorpusReader('./VTB_utf8/', '.*')
train_corpus = []
test_corpus = []
for (fileid, value) in enumerate(wordlists.fileids()):
    if fileid < 714/2:
        file_train = open('./VTB_utf8/' + value, 'r', encoding='utf-8').read()
        file_train = file_train.split()
        for ft in file_train:
            temp = '/'.join(ft.split('/', 2)[:2])
            train_corpus.append(temp)
    # elif fileid >= 714/2:
    #     test_corpus = open('./VTB_utf8/' + value, 'r', encoding='utf-8').read()
    #     test_corpus = test_corpus.split()
    #     for ft in test_corpus:
    #         temp = '/'.join(ft.split('/', 2)[:2])
    #         test_corpus.append(temp)

train_corpus = [nltk.tag.str2tuple(s) for s in train_corpus]
unigram_tagger = nltk.UnigramTagger(train_corpus) # train trên 1 list chứa list câu
'''
'''
Chapter 6
'''

# def gender_feature(word):
#     return {'last_letter': word[-1]}

# from nltk.corpus import names
# import random

# names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
# random.shuffle(names)

# featuresets =  [(gender_feature(n), g) for (n, g) in names] # có thể đặt nhiều feature, nhưng theo dạng từ điển
# train_set, test_set = featuresets[500:], featuresets[:500]
# classifier = nltk.NaiveBayesClassifier.train(train_set)

# print(classifier.classify(gender_feature('Johnny')))
# print(nltk.classify.accuracy(classifier, test_set))

'''
When working with large corpora, constructing a single list that contains the features
of every instance can use up a large amount of memory. In these cases, use the function
nltk.classify.apply_features, which returns an object that acts like a list but does not
store all the feature sets in memory:
'''
# from nltk.classify import apply_features
# train_set = apply_features(gender_feature, names[500:])
# test_set = apply_features(gender_feature, names[:500])

'''
Chapter 7
'''
# Example of a simple regular expression–based NP chunker
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),  ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]

grammar = "NP: {<DT>?<JJ>*<NN>}"

grammar2 = r"""
    NP: {<DT|PP\$>?<JJ>*<NN>}
        {<NNP>+} 
"""

grammar3 = r"""
 NP: {<DT|JJ|NN.*>+} # Chunk sequences of DT, JJ, NN
 PP: {<IN><NP>} # Chunk prepositions followed by NP
 VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
 CLAUSE: {<NP><VP>} # Chunk NP, VP
 """

# cp = nltk.RegexpParser(grammar)
# cp2 = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
# cp3 = nltk.RegexpParser(grammar, loop=2)
# result = cp.parse(sentence)
# # print(result)
# result.draw()

'''
Chapter 8 -> 10: phân tích ngữ nghĩa và cấu trúc (grammar) của câu
Chapter 11: nói về phonetic, các kiểu lưu dữ liệu
'''
