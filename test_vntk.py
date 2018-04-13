from vntk import vnnews
import nltk
import tkinter as tk
from tkinter import ttk, StringVar
from tkinter.filedialog import *

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

        for F in (StartPage, DispersionPlot):
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

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Vietnamese Toolkit", font=LARGE_FONT)
        label.grid(row=0, column=150)
       
        button = tk.Button(self, text="Dispersion Plot",
                            command=lambda: controller.show_frame(DispersionPlot))
        button.grid(row=1, column=0)

        global RAW_BUTTON, ID_BUTTON, WORD_BUTTON, TAGGED_WORD_BUTTON

        ID_BUTTON = ttk.Button(self, text='ID files',state=DISABLED, command=fileId)
        ID_BUTTON.grid(row=2, column=0)

        RAW_BUTTON = ttk.Button(self, text='Raw',state=DISABLED, command=raw)
        RAW_BUTTON.grid(row=3, column=0)

        WORD_BUTTON = ttk.Button(self, text='Word',state=DISABLED, command=word)
        WORD_BUTTON.grid(row=4, column=0)

        TAGGED_WORD_BUTTON = ttk.Button(self, text='Tagged Word',state=DISABLED, command=taggedWord)
        TAGGED_WORD_BUTTON.grid(row=5, column=0)

class DispersionPlot(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Dispersion Plot", font=LARGE_FONT)
        label.grid(row=0, column=150)

        button2 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=1, column=0)

        global OK_BUTTON

        OK_BUTTON = ttk.Button(self, text='Dispersion Button',state=DISABLED, command=dispersionPlot)
        OK_BUTTON.grid(row=2, column=0)

app = VNTK()
app.geometry("720x680")
app.mainloop()

# test = vnnews()

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

