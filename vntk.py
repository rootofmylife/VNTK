import nltk
from nltk.corpus import PlaintextCorpusReader

class vnnews:
    def __init__(self, file_path):
        self.name_corpus = []
        self.file_path = file_path
        wordlists = PlaintextCorpusReader(file_path, '.*')
        for (fileid, value) in enumerate(wordlists.fileids()): # fileids([categories])
           self.name_corpus.append(str(value))
        pass

    def fileids(self):
        self.name_corpus = []
        wordlists = PlaintextCorpusReader(self.file_path, '.*')
        for (fileid, value) in enumerate(wordlists.fileids()): # fileids([categories])
           self.name_corpus.append(str(value))
        return self.name_corpus

    def raws(self, file_id = ''):
        if len(file_id) == 0:
            words = []
            str_raw = ''
            for i in self.name_corpus:
                corpus = open(self.file_path+ i, 'r', encoding='utf-8').read()
                temp = corpus.split()
                temp2 = [s.split('/')[0] for s in temp]
                str_raw += ' '.join(temp2) + '\n'
            return str_raw
        else:
            corpus = open(self.file_path + file_id, 'r', encoding='utf-8').read()
            temp = corpus.split()
            temp2 = [s.split('/')[0] for s in temp]
            return ' '.join(temp2)

    def words(self, file_id = ''):
        if len(file_id) == 0:
            words = []
            for i in self.name_corpus:
                corpus = open(self.file_path + i, 'r', encoding='utf-8').read()
                temp = corpus.split()
                temp2 = [s.split('/')[0] for s in temp]
                for k in temp2:
                    words.append(k)
            return words
        else:
            corpus = open(self.file_path + file_id, 'r', encoding='utf-8').read()
            temp = corpus.split()
            words.append([s.split('/')[0] for s in temp])
            return words

    def tagged_words(self, file_id = ''):
        if len(file_id) == 0:
            words = []
            for i in self.name_corpus:
                corpus = open(self.file_path + i, 'r', encoding='utf-8').read()
                temp = corpus.split()
                temp2 = [(s.split('/')[0], s.split('/')[1]) for s in temp]
                for k in temp2:
                    words.append(k)
            return words
        else:
            corpus = open(self.file_path + file_id, 'r', encoding='utf-8').read()
            temp = corpus.split()
            words.append([(s.split('/')[0], s.split('/')[1]) for s in temp])
            return words

class pos_tag:
    pass

class sent_tokenize:
    pass

# # làm dựa trên corpus hiện có
class NER:
    pass

# chắc k làm, có làm thì dựa trên corpus hiện có
class word_tokenize:
    pass

# làm dựa trên corpus hiện có
class chunking:
    pass