import nltk
from nltk.corpus import PlaintextCorpusReader

class vntk(object):
    def __init__(self, path):
        self.path = path

    def load_corpus(self):
        wordlists = PlaintextCorpusReader(self.path, '.*')
        for (fileid, value) in enumerate(wordlists.fileids()): # fileids([categories])
           print('text' + str(fileid) + ': ' + str(value))

    def open_corpus(path_corpus):
        cp = open(path_corpus, 'r', encoding='utf-8').read()
        return cp

# có thể thay "corpus" = tên của 1 data, vd: nguyen_nhat_anh
class Corpus(object):
    def __init__(self, corpus):
        # từ đã được tokenized
        token = nltk.word_tokenize(corpus)
        self.corpus = nltk.Text(token)

    # tìm những khúc chứa những từ này
    def concordance(self, key):
        print(self.corpus.concordance(key))

    # tìm những câu có cùng ngữ cảnh với từ này, giống y hệt
    def similar(self, key):
        print(self.corpus.similar(key))

    # examine just the contexts that are shared by two or more words
    def common_contexts(self, key1, key2):
        print(self.corpus.common_contexts(key1, key2))

    def count_token(self):
        return len(self.corpus)

    def count_1_token(self):
        return len(set(self.corpus))

    # đếm số lần xuất hiện
    def count(self, key):
        return self.corpus.count(key)

    def sents(self):
        return nltk.sent_tokenize(self.corpus)

    def words(self):
        return nltk.word_tokennize(self.corpus)
        

class Analysis(object):
    def __init__(self, corpus):
        # từ đã được tokenized
        token = nltk.word_tokenize(corpus)
        self.corpus = nltk.Text(token)

    # trả về từ điển tần số xuất hiện của 1 từ
    def freq_dict(self):
        return nltk.FreqDist(self.corpus)

    def max_freq(self):
        return nltk.FreqDist(self.corpus).max()

    def one_freq(self):
        print(nltk.FreqDist(self.corpus).hapaxes())

    def collocation(self):
        print(self.corpus.collocations())

    def bigram(sentence):
        return nltk.bigrams(sentence)