import nltk
from nltk.corpus import PlaintextCorpusReader

# vntk.vnnews.raws()
# vntk.vnnews.words()
class vnnews:
    def __init__(self):
        self.name_corpus = []
        wordlists = PlaintextCorpusReader('./VTB_utf8/', '.*')
        for (fileid, value) in enumerate(wordlists.fileids()): # fileids([categories])
           self.name_corpus.append(str(value))

    def fileids(self):
        return self.name_corpus

    def raws(self, file_id = ''):
        if len(file_id) == 0:
            words = []
            str_raw = ''
            for i in self.name_corpus:
                corpus = open('./VTB_utf8/' + i, 'r', encoding='utf-8').read()
                temp = corpus.split()
                temp2 = [s.split('/')[0] for s in temp]
                str_raw += ' '.join(temp2) + '\n'
            return str_raw
        else:
            corpus = open('./VTB_utf8/' + file_id, 'r', encoding='utf-8').read()
            temp = corpus.split()
            temp2 = [s.split('/')[0] for s in temp]
            return ' '.join(temp2)

    def words(self, file_id = ''):
        if len(file_id) == 0:
            words = []
            for i in self.name_corpus:
                corpus = open('./VTB_utf8/' + i, 'r', encoding='utf-8').read()
                temp = corpus.split()
                temp2 = [s.split('/')[0] for s in temp]
                for k in temp2:
                    words.append(k)
            return nltk.Text(words)
        else:
            corpus = open('./VTB_utf8/' + file_id, 'r', encoding='utf-8').read()
            temp = corpus.split()
            words.append([s.split('/')[0] for s in temp])
            return nltk.Text(words)

    def tagged_words(self, file_id = ''):
        if len(file_id) == 0:
            words = []
            for i in self.name_corpus:
                corpus = open('./VTB_utf8/' + i, 'r', encoding='utf-8').read()
                temp = corpus.split()
                temp2 = [(s.split('/')[0], s.split('/')[1]) for s in temp]
                for k in temp2:
                    words.append(k)
            return words
        else:
            corpus = open('./VTB_utf8/' + file_id, 'r', encoding='utf-8').read()
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