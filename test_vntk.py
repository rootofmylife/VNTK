from vntk import vnnews
import nltk
import tkinter as tk
from tkinter import ttk, StringVar
from tkinter.filedialog import *
from cPickle import dump, load

LARGE_FONT= ("Verdana", 12)

def chooseFilePath():
    global dataAnalysisCorpus
    filename = askdirectory() + '/'
    dataAnalysisCorpus = vnnews(filename)
    OK_BUTTON.config(state='normal')
    RAW_BUTTON.config(state='normal')
    ID_BUTTON.config(state='normal')
    WORD_BUTTON.config(state='normal')
    TAGGED_WORD_BUTTON.config(state='normal')
    CONCORDANCE_BUTTON.config(state='normal')
    SIMILAR_BUTTON.config(state='normal')
    FREDIST_BUTTON.config(state='normal')
    SEARCH_BUTTON.config(state='normal')
    CUMULATIVE_BUTTON.config(state='normal')
    HAPAXAES_BUTTON.config(state='normal')

class VNTK(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Vietnamese Toolkit v0.0.1")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # menu bar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open File", command=chooseFilePath)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, DispersionPlot, SimpleTool, FrequencyDitribution, trainingLearning, wordSegmentation, sentSegmentation, POS):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # frame = StartPage(container, self)
        # self.frames[StartPage] = frame
        # frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def dispersionPlot():
    arr = ['thông_tin', 'chính_phủ', 'những']
    nltk.Text(dataAnalysisCorpus.words()).dispersion_plot(arr)

def raw():
    stringText = dataAnalysisCorpus.raws()
    showedText = Text()
    showedText.insert(END, stringText)
    showedText.pack()

def fileId():
    arrayID = dataAnalysisCorpus.fileids()
    showedText = Text()
    for i in arrayID:
        showedText.insert(END, i + '\n')
    showedText.pack()

def word():
    arrayWord = dataAnalysisCorpus.words()
    showedText = Text()
    for i in arrayWord:
        showedText.insert(END, i + '\n')
    showedText.pack()

def taggedWord():
    arrayTaggedWord = dataAnalysisCorpus.tagged_words()
    showedText = Text()
    for i in arrayTaggedWord:
        str_temp = '(' + str(i[0]) + ',' + str(i[1]) + ')'
        showedText.insert(END, str_temp + '\n')
    showedText.pack()

# kiểm tra là array hay gì từ function này trở xuống
def concordanceFunction():
    arrCon = nltk.Text(dataAnalysisCorpus.words()).concordance('thông_tin')
    showedText = Text()
    for i in arrCon:
        showedText.insert(END, i + '\n')
    showedText.pack()

def similarFunction():
    arrCon = nltk.Text(dataAnalysisCorpus.words()).similar('thông_tin')
    showedText = Text()
    for i in arrCon:
        showedText.insert(END, i + '\n')
    showedText.pack()

def freqDistFucntion():
    global fdist
    arrFreq = nltk.FreqDist(nltk.Text(dataAnalysisCorpus.words()))
    fdist = arrFreq
    showedText = Text()
    for i in arrFreq:
        str_temp = str(i) + ': ' + arrFreq[i]
        showedText.insert(END, str_temp + '\n' )
    showedText.pack()

def searchFunction():
    showedText = Text()
    showedText.insert(END, str(fdist['thông_tin']))
    showedText.pack()

def cumulativeFunction():
    fdist.plot(50, cumulative=True)

def hapaxesFunction():
    showedText = Text()
    arrhapaxes = fdist.hapaxes()
    for i in arrhapaxes:
        showedText.insert(END, i + '\n')
    showedText.pack()

def wordCountFunction():
    showedText = Text()
    showedText.insert(END, str(len(nltk.Text(dataAnalysisCorpus.words()))))
    showedText.pack()

def trainPOS():
    # upload file function, file đã dc annotated
    # word_segment -> sent_segment

    train_set = [('a', 'DT')]
    t0 = nltk.DefaultTagger('UNK')
    t1 = nltk.UnigramTagger(train_set, backoff=t0)
    t2 = nltk.BigramTagger(train_set, backoff=t1)
    t3 = nltk.TrigramTagger(train_set, backoff=t2)

    output = open('POStagger.pkl', 'wb')
    dump(t3, output, -1)
    output.close()

def trainWordSegment():
    # tách ra các cạp từ đã được tách sẵn
    train_set = [('thông', 'tin')]
    t0 = nltk.DefaultTagger('UNK')
    t1 = nltk.UnigramTagger(train_set, backoff=t0)
    t2 = nltk.BigramTagger(train_set, backoff=t1)
    t3 = nltk.TrigramTagger(train_set, backoff=t2)

    output = open('wordSegment.pkl', 'wb')
    dump(t3, output, -1)
    output.close()

# tới đây
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Vietnamese Toolkit", font=LARGE_FONT)
        label.grid(row=0, column=0)
       
        buttonHome = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        buttonHome.grid(row=1, column=0)

        button = ttk.Button(self, text="Dispersion Plot", width=12,
                            command=lambda: controller.show_frame(DispersionPlot))
        button.grid(row=1, column=1)

        button2 = ttk.Button(self, text="Simple Tool", width=12,
                            command=lambda: controller.show_frame(SimpleTool))
        button2.grid(row=1, column=2)

        button3 = ttk.Button(self, text="Frequency Tool", width=12,
                            command=lambda: controller.show_frame(FrequencyDitribution))
        button3.grid(row=1, column=3)
        
        #sửa hàm

        button4 = ttk.Button(self, text="Train/Learn Tool", width=12,
                            command=lambda: controller.show_frame(trainingLearning))
        button4.grid(row=1, column=4)

        button5 = ttk.Button(self, text="Word Segment", width=12,
                            command=lambda: controller.show_frame(wordSegmentation))
        button5.grid(row=1, column=5)

        button6 = ttk.Button(self, text="Sent Segment", width=12,
                            command=lambda: controller.show_frame(sentSegmentation))
        button6.grid(row=1, column=6)

        button7 = ttk.Button(self, text="POS", width=12,
                            command=lambda: controller.show_frame(POS))
        button7.grid(row=1, column=7)
        #=======
        global RAW_BUTTON, ID_BUTTON, WORD_BUTTON, TAGGED_WORD_BUTTON

        ID_BUTTON = ttk.Button(self, text='ID files',state=DISABLED, width=12, command=fileId)
        ID_BUTTON.grid(row=2, column=0)

        RAW_BUTTON = ttk.Button(self, text='Raw',state=DISABLED, width=12, command=raw)
        RAW_BUTTON.grid(row=3, column=0)

        WORD_BUTTON = ttk.Button(self, text='Word',state=DISABLED, width=12, command=word)
        WORD_BUTTON.grid(row=4, column=0)

        TAGGED_WORD_BUTTON = ttk.Button(self, text='Tagged Word',state=DISABLED, width=12, command=taggedWord)
        TAGGED_WORD_BUTTON.grid(row=5, column=0)

class DispersionPlot(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Dispersion Plot", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button2 = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=1, column=0)

        global OK_BUTTON

        OK_BUTTON = ttk.Button(self, text='Dispersion',state=DISABLED, width=12, command=dispersionPlot)
        OK_BUTTON.grid(row=2, column=0)

class SimpleTool(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Simple Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button3 = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        button3.grid(row=1, column=0)

        global CONCORDANCE_BUTTON, SIMILAR_BUTTON, WORDCOUNT_BUTTON

        CONCORDANCE_BUTTON = ttk.Button(self, text='Concordance',state=DISABLED, width=12, command=concordanceFunction)
        CONCORDANCE_BUTTON.grid(row=2, column=0)

        SIMILAR_BUTTON = ttk.Button(self, text='Similar',state=DISABLED, width=12, command=similarFunction)
        SIMILAR_BUTTON.grid(row=3, column=0)

        WORDCOUNT_BUTTON = ttk.Button(self, text='Word Count',state=DISABLED, width=12, command=wordCountFunction)
        WORDCOUNT_BUTTON.grid(row=4, column=0)

class FrequencyDitribution(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Frequency Distribution Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button4 = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        button4.grid(row=1, column=0)

        global FREDIST_BUTTON, SEARCH_BUTTON, CUMULATIVE_BUTTON, HAPAXAES_BUTTON

        FREDIST_BUTTON = ttk.Button(self, text='FreqDist',state=DISABLED, width=12, command=freqDistFucntion)
        FREDIST_BUTTON.grid(row=2, column=0)

        SEARCH_BUTTON = ttk.Button(self, text='Search',state=DISABLED, width=12, command=searchFunction)
        SEARCH_BUTTON.grid(row=3, column=0)

        CUMULATIVE_BUTTON = ttk.Button(self, text='Cumulative Plot',state=DISABLED, width=12, command=cumulativeFunction)
        CUMULATIVE_BUTTON.grid(row=4, column=0)

        HAPAXAES_BUTTON = ttk.Button(self, text='Hapaxaes',state=DISABLED, width=12, command=hapaxesFunction)
        HAPAXAES_BUTTON.grid(row=5, column=0)

class trainingLearning(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Training/Learning Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button5 = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        button5.grid(row=1, column=0)

class wordSegmentation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Word Segmentation Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button6 = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        button6.grid(row=1, column=0)

class sentSegmentation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Sentence Segmentation Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button7 = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        button7.grid(row=1, column=0)

class POS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="POS Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button8 = ttk.Button(self, text="Home", width=12,
                            command=lambda: controller.show_frame(StartPage))
        button8.grid(row=1, column=0)

app = VNTK()
app.geometry("860x720")
app.mainloop()

# test = vnnews()
'''
chuyển sang nltk.Text()
'''
# print(test.raws())
# print(test.fileids())
# print(test.words())
# print(test.tagged_words())

# print(test.words().concordance('thông_tin'))
# print(test.words().similar('thông_tin'))
# print(test.words().common_contexts(['ngâm', 'đau']))

# tần số của từ
# print(nltk.FreqDist(test.words()))
# print(fdist.keys()) # in ra bộ từ vựng
# print(fdist['ngâm']) # lấy ra tần số suất hiện của từ này
# fdist.plot(50, cumulative=True) # graph về tần số của 50 từ đầu tiên
# print(fdist.hapaxes()) # in ra những từ xuất hiện 1 lần
# fdist.freq('monstrous') # Frequency of a given sample
# fdist.N() # Total number of samples
# for sample in fdist: # Iterate over the samples, in order of decreasing frequency
# fdist.max() # Sample with the greatest count
# fdist.tabulate() # Tabulate the frequency distribution
# print(corpus.collocations()) # tìm ra các cặp câu, mà có số lần xuất hiện nhiều hơn 1 từ trong câu đó


# a dispersion plot
# test.words().dispersion_plot(['thông_tin', 'chính_phủ', 'những'])

# count word
# print(len(test.words()))

