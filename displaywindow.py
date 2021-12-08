import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from poetrystyles import poem_type
from poetrystyles import identify_rhyme_scheme
from syllablecounter import syllable_counter
from rhyme import rhyme_suggestion

def saveFiles():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt")],)
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)

def openFiles():
    filepath=tk.filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text files","*.txt*")],)
    with open(filepath, "r") as input_file:
        text=input_file.read()
        txt_edit.delete("1.0", "end")
        txt_edit.insert(tk.END, text)

def StyleIndentifier():
    filepath = tk.filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text files", "*.txt*")], )
    with open(filepath, "r") as input_file:
        text = input_file.read()
        #poem_type(text) #input is string
        newWindow=Toplevel(window)
        newWindow.title("Poem Style")
        newWindow.geometry("200x100")
        Label(newWindow, text=poem_type()).pack()

def SyllableCounter():
    newWindow = Toplevel(window)
    newWindow.title("Syllable Counter")
    newWindow.geometry("350x100")
    userInput = Entry(newWindow, width=40, justify=CENTER)
    userInput.insert(END, "Enter a word")
    userInput.grid(row=0, columnspan=3, padx=5, pady=10)
    wordinput=str(userInput)
    def finalcount():
        syllables=str(syllable_counter(wordinput))
        userInput.delete(0, "end")
        userInput.insert(0, syllables)
    Button(newWindow, text="Syllable Count", command=finalcount).grid(row=1, column=1)

def RhymeSuggestion():
    newWindow = Toplevel(window)
    newWindow.title("Rhyme Suggester")
    newWindow.geometry("350x100")
    userInput = Entry(newWindow, width=40, justify=CENTER)
    userInput.insert(END, "Enter a word")
    userInput.grid(row=0, columnspan=3, padx=5, pady=10)
    wordinput = str(userInput)
    def suggester():
        newnewWindow = Toplevel(window)
        Label(newnewWindow, text=()).pack()




window = tk.Tk()
window.title("Poem Analyzer")

txt_edit = tk.Text(window)
txt_edit.insert(END, "Save file as 'user_poem'")
fr_buttons = tk.Frame(window, relief=tk.RAISED)
btn_save = tk.Button(fr_buttons, text="Save As...", command=saveFiles)
btn_open = tk.Button(fr_buttons, text="Open", command=openFiles)
btn_style = tk.Button(fr_buttons, text="Poem Style", command=StyleIndentifier)
btn_syllable = tk.Button(fr_buttons, text="Syllable Counter", command=SyllableCounter)

btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_open.grid(row=0, column=0, sticky="ew", padx=5)
btn_style.grid(row=2, column=0, sticky="ew", padx=5)
btn_syllable.grid(row=3, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()



#h = open("user_poem.txt", "r")
#fh
#s = fh.read()
#s
#'It may be that the gulfs will wash us down:\nIt may be we shall touch the Happy Isles,\nAnd see the great Achilles, whom we knew.\nTho much is taken, much abides; and tho\nWe are not now that strength which in old days\nMoved earth and heaven, that which we are, we are;\nOne equal temper of heroic hearts,\nMade weak by time and fate, but strong in will\nTo strive, to seek, to find, and not to yield.'
#s.split("\n")