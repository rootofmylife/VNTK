from vntk import vnnews
from _pickle import dump, load
import nltk
import tkinter as tk
from tkinter import ttk, StringVar
from tkinter.filedialog import *
from nltk.text import ConcordanceIndex

LARGE_FONT= ("Verdana", 12)

# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

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
    # SIMILAR_BUTTON.config(state='normal')
    WORDCOUNT_BUTTON.config(state='normal')
    FREDIST_BUTTON.config(state='normal')
    SEARCH_BUTTON.config(state='normal')
    CUMULATIVE_BUTTON.config(state='normal')
    HAPAXAES_BUTTON.config(state='normal')

def dispersionPlot(getData):
    getData = getData.split(',')
    getData = [s.strip() for s in getData]
    nltk.Text(dataAnalysisCorpus.words()).dispersion_plot(getData)

def raw():
    showedText.delete('1.0', END)
    stringText = dataAnalysisCorpus.raws()
    showedText.insert(END, stringText)   

def fileId():
    showedText.delete('1.0', END)
    arrayID = dataAnalysisCorpus.fileids()
    for i in arrayID:
        showedText.insert(END, i + '\n')

def word():
    showedText.delete('1.0', END)
    arrayWord = dataAnalysisCorpus.words()
    for i in arrayWord:
        showedText.insert(END, i + '\n')

def taggedWord():
    showedText.delete('1.0', END)
    arrayTaggedWord = dataAnalysisCorpus.tagged_words()
    for i in arrayTaggedWord:
        str_temp = '(' + str(i[0]) + ',' + str(i[1]) + ')'
        showedText.insert(END, str_temp + '\n')

def concordance(ci, word, width=75, lines=25):
    """
    Rewrite of nltk.text.ConcordanceIndex.print_concordance that returns results
    instead of printing them. 

    See:
    http://www.nltk.org/api/nltk.html#nltk.text.ConcordanceIndex.print_concordance
    """
    half_width = (width - len(word) - 2) // 2
    context = width // 4 # approx number of words of context

    results = []
    offsets = ci.offsets(word)
    if offsets:
        lines = min(lines, len(offsets))
        for i in offsets:
            if lines <= 0:
                break
            left = (' ' * half_width +
                    ' '.join(ci._tokens[i-context:i]))
            right = ' '.join(ci._tokens[i+1:i+context])
            left = left[-half_width:]
            right = right[:half_width]
            results.append('%s %s %s' % (left, ci._tokens[i], right))
            lines -= 1

    return results

def concordanceFunction(data):
    showedText2.delete('1.0', END)
    arrCon = ConcordanceIndex(nltk.Text(dataAnalysisCorpus.words()))
    arr = concordance(arrCon, data)

    for i in arr:
         showedText2.insert(END, i + '\n')

def similarFunction(data):
    showedText.delete('1.0', END)
    arrCon = nltk.Text(dataAnalysisCorpus.words()).similar(data.strip())
    print(arrCon)
    # showedText = Text()
    # for i in arrCon:
    #     showedText.insert(END, i + '\n')
    # showedText.pack()

def freqDistFucntion(): 
    showedText3.delete('1.0', END)
    arrFreq = nltk.FreqDist(nltk.Text(dataAnalysisCorpus.words()))
    for i in arrFreq:
        str_temp = str(i) + ': ' + str(arrFreq[i])
        showedText3.insert(END, str_temp + '\n' )

def searchFunction(data):
    showedText3.delete('1.0', END)
    showedText3.insert(END, str(nltk.FreqDist(nltk.Text(dataAnalysisCorpus.words()))[data]))

def cumulativeFunction(data):
    nltk.FreqDist(nltk.Text(dataAnalysisCorpus.words())).plot(int(data), cumulative=True)

def hapaxesFunction():
    showedText3.delete('1.0', END)
    arrhapaxes = nltk.FreqDist(nltk.Text(dataAnalysisCorpus.words())).hapaxes()
    for i in arrhapaxes:
        showedText3.insert(END, i + '\n')

def wordCountFunction():
    showedText2.delete('1.0', END)
    showedText2.insert(END, str(len(nltk.Text(dataAnalysisCorpus.words()))))

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

        filemenu2 = tk.Menu(menubar, tearoff=0)
        filemenu2.add_command(label="Dispersion Plot", command= lambda: self.show_frame(DispersionPlot))
        filemenu2.add_command(label="Simple Tool", command= lambda: self.show_frame(SimpleTool))
        filemenu2.add_command(label="Frequency Tool", command= lambda: self.show_frame(FrequencyDitribution))
        filemenu2.add_command(label="Train/Learn Tool", command= lambda: self.show_frame(trainingLearning))
        filemenu2.add_command(label="Word Segment", command= lambda: self.show_frame(wordSegmentation))
        filemenu2.add_command(label="Sent Segment", command= lambda: self.show_frame(sentSegmentation))
        filemenu2.add_command(label="POS", command= lambda: self.show_frame(POS))
        menubar.add_cascade(label="Tools", menu=filemenu2)

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

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        '''
        # buttonHome = ttk.Button(self, text="Home", width=18)
        # buttonHome.grid(row=0, column=0)

        # button = ttk.Button(self, text="Dispersion Plot", width=18,
        #                     command=lambda: controller.show_frame(DispersionPlot))
        # button.grid(row=1, column=0)

        # button2 = ttk.Button(self, text="Simple Tool", width=18,
        #                     command=lambda: controller.show_frame(SimpleTool))
        # button2.grid(row=1, column=2)

        # button3 = ttk.Button(self, text="Frequency Tool", width=18,
        #                     command=lambda: controller.show_frame(FrequencyDitribution))
        # button3.grid(row=1, column=3)
        
        # #sửa hàm

        # button4 = ttk.Button(self, text="Train/Learn Tool", width=18,
        #                     command=lambda: controller.show_frame(trainingLearning))
        # button4.grid(row=1, column=4)

        # button5 = ttk.Button(self, text="Word Segment", width=18,
        #                     command=lambda: controller.show_frame(wordSegmentation))
        # button5.grid(row=1, column=5)

        # button6 = ttk.Button(self, text="Sent Segment", width=18,
        #                     command=lambda: controller.show_frame(sentSegmentation))
        # button6.grid(row=1, column=6)

        # button7 = ttk.Button(self, text="POS", width=18,
        #                     command=lambda: controller.show_frame(POS))
        # button7.grid(row=1, column=7)
        #=======
        '''
        global RAW_BUTTON, ID_BUTTON, WORD_BUTTON, TAGGED_WORD_BUTTON, showedText

        showedText = Text(self, height=15)

        ID_BUTTON = ttk.Button(self, text='ID files',state=DISABLED, width=18, command=fileId)
        ID_BUTTON.grid(row=0, column=0)

        RAW_BUTTON = ttk.Button(self, text='Raw',state=DISABLED, width=18, command=raw)
        RAW_BUTTON.grid(row=1, column=0)

        WORD_BUTTON = ttk.Button(self, text='Word',state=DISABLED, width=18, command=word)
        WORD_BUTTON.grid(row=2, column=0)

        TAGGED_WORD_BUTTON = ttk.Button(self, text='Tagged Word',state=DISABLED, width=18, command=taggedWord)
        TAGGED_WORD_BUTTON.grid(row=3, column=0)

        showedText.grid(row=0, column=1, rowspan=20)

class DispersionPlot(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        button2 = ttk.Button(self, text="Home", width=18,
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=1, column=0)

        v = StringVar()
        e = Entry(self, textvariable=v)
        e.grid(row=2, column=0)

        global OK_BUTTON

        OK_BUTTON = ttk.Button(self, text='Dispersion',state=DISABLED, width=18, command= lambda: dispersionPlot(v.get()))
        OK_BUTTON.grid(row=3, column=0)

class SimpleTool(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        button3 = ttk.Button(self, text="Home", width=18,
                            command=lambda: controller.show_frame(StartPage))
        button3.grid(row=1, column=0)

        global CONCORDANCE_BUTTON, SIMILAR_BUTTON, WORDCOUNT_BUTTON, showedText2

        showedText2 = Text(self, height=15)

        v = StringVar()
        e = Entry(self, textvariable=v, width=18)
        e.grid(row=2, column=0)

        CONCORDANCE_BUTTON = ttk.Button(self, text='Concordance',state=DISABLED, width=18, command= lambda: concordanceFunction(v.get()))
        CONCORDANCE_BUTTON.grid(row=3, column=0)

        # để làm sau
        # v2 = StringVar()
        # e2 = Entry(self, textvariable=v2)
        # e2.grid(row=4, column=0)

        # SIMILAR_BUTTON = ttk.Button(self, text='Similar',state=DISABLED, width=18, command= lambda: similarFunction(v.get()))
        # SIMILAR_BUTTON.grid(row=5, column=0)

        WORDCOUNT_BUTTON = ttk.Button(self, text='Word Count',state=DISABLED, width=18, command=wordCountFunction)
        WORDCOUNT_BUTTON.grid(row=4, column=0)

        showedText2.grid(row=0, column=1, rowspan=20)

class FrequencyDitribution(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        button4 = ttk.Button(self, text="Home", width=18,
                            command=lambda: controller.show_frame(StartPage))
        button4.grid(row=1, column=0)

        global FREDIST_BUTTON, SEARCH_BUTTON, CUMULATIVE_BUTTON, HAPAXAES_BUTTON, showedText3

        showedText3 = Text(self, height=15)

        FREDIST_BUTTON = ttk.Button(self, text='FreqDist',state=DISABLED, width=18, command=freqDistFucntion)
        FREDIST_BUTTON.grid(row=2, column=0)

        v2 = StringVar()
        e2 = Entry(self, textvariable=v2, width=18)
        e2.grid(row=3, column=0)

        SEARCH_BUTTON = ttk.Button(self, text='Search',state=DISABLED, width=18, command= lambda: searchFunction(e2.get()))
        SEARCH_BUTTON.grid(row=4, column=0)

        v3 = StringVar()
        e3 = Entry(self, textvariable=v3, width=18)
        e3.grid(row=5, column=0)

        CUMULATIVE_BUTTON = ttk.Button(self, text='Cumulative Plot',state=DISABLED, width=18, command= lambda: cumulativeFunction(e3.get()))
        CUMULATIVE_BUTTON.grid(row=6, column=0)

        HAPAXAES_BUTTON = ttk.Button(self, text='Hapaxaes',state=DISABLED, width=18, command=hapaxesFunction)
        HAPAXAES_BUTTON.grid(row=7, column=0)

        showedText3.grid(row=0, column=1, rowspan=20)

class trainingLearning(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Training/Learning Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button5 = ttk.Button(self, text="Home", width=18,
                            command=lambda: controller.show_frame(StartPage))
        button5.grid(row=1, column=0)

class wordSegmentation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Word Segmentation Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button6 = ttk.Button(self, text="Home", width=18,
                            command=lambda: controller.show_frame(StartPage))
        button6.grid(row=1, column=0)

class sentSegmentation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Sentence Segmentation Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button7 = ttk.Button(self, text="Home", width=18,
                            command=lambda: controller.show_frame(StartPage))
        button7.grid(row=1, column=0)

class POS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="POS Tool", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button8 = ttk.Button(self, text="Home", width=18,
                            command=lambda: controller.show_frame(StartPage))
        button8.grid(row=1, column=0)

app = VNTK()
app.geometry("770x255")
app.mainloop()