import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from poetrystyles import poem_type
from poetrystyles import identify_rhyme_scheme
from syllablecounter import syllable_counter
from rhyme import rhyme_suggestion


def saveFiles():
    """
    This function allows the user to save the text written in the display window text box as a text file
    """
    #filepath that opens file manager and asks user to save file under specific name and in specified place
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt")],)

    #opening the file, which is blank
    with open(filepath, "w") as output_file:

        #inserting the text box text into the file and saving
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)

def openFiles():
    """
    This function allows the user to open a text file and edit it in the display window text box
    """
    #filepath that opens file manager and asks user to open a specific file
    filepath=tk.filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text files","*.txt*")],)

    #opening and reading the file
    with open(filepath, "r") as input_file:

        #inserting the lines from the file into the displayed text box
        text=input_file.read()
        txt_edit.delete("1.0", "end")
        txt_edit.insert(tk.END, text)

def StyleIndentifier():
    """
    This function asks the user to open a file and returns the style of poem that text file is in
    """
    #asking the user to open a specific file
    filepath = tk.filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text files", "*.txt*")], )

    #opening and reading the file
    with open(filepath, "r") as input_file:
        input_file.read()

        #opening a new display window that displays the output of poem_type on the user_poem file
        newWindow=Toplevel(window)
        newWindow.title("Poem Style")
        newWindow.geometry("700x200")
        Label(newWindow, text=poem_type(), font=('Arial',60)).pack()

def SyllableCounter():
    """
    This function opens a window allowing the user to type a word and displays the number of syllables in that word
    """
    #opening new window
    newWindow = Toplevel(window)
    newWindow.title("Syllable Counter")
    newWindow.geometry("350x100")
    userInput = Entry(newWindow, width=40, justify=CENTER)
    userInput.insert(END, "Enter a word")
    userInput.grid(row=0, columnspan=3, padx=5, pady=10)

    #creating function for the button command thats inside this new window
    def finalcount():
        #running syllable_counter on the current text inside the text box in the new window
        syllables=str(syllable_counter(userInput.get()))

        #deleting the written word and displaying the return from syllable_counter
        userInput.delete(0, "end")
        userInput.insert(0, syllables)

    #creating button to run the function
    Button(newWindow, text="Syllable Count", command=finalcount).grid(row=1, column=1)

def RhymeSuggestion():
    """
    This function opens a window where the user can input a word and another window will display a suggestion for another
    word to rhyme with the inputted word
    """
    #opening a new window
    newWindow = Toplevel(window)
    newWindow.title("Rhyme Suggester")
    newWindow.geometry("350x100")
    userInput = Entry(newWindow, width=40, justify=CENTER)
    userInput.insert(END, "Enter a word (All uppercase)")
    userInput.grid(row=0, columnspan=3, padx=5, pady=10)

    #creating function for button command that runs rhyme_suggestion on the inputted word
    def suggester():
        newnewWindow = Toplevel(window)
        newnewWindow.geometry("200x100")
        Label(newnewWindow, text=(rhyme_suggestion(userInput.get()))).pack()

    #creating button to run suggester
    Button(newWindow, text="Find a rhyming word", command=suggester).grid(row=1, column=1)

def RhymeStyleIdentifier():
    #asking the user to open a specific file
    filepath = tk.filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text files", "*.txt*")], )

    #reading the file
    with open(filepath, "r") as input_file:
        input_file.read()

        #displaying new window
        newWindow = Toplevel(window)
        newWindow.title("Rhyme Style")
        newWindow.geometry("700x200")

        #inserting return of indentify_rhyme_scheme in the window
        Label(newWindow, text=identify_rhyme_scheme(), font=('Arial', 60)).pack()


#creating display window and title
window = tk.Tk()
window.title("Poem Analyzer")

#adding text box and initial text
txt_edit = tk.Text(window)
txt_edit.insert(END, "Save file as 'user_poem'")

#creating buttons for each function
fr_buttons = tk.Frame(window, relief=tk.RAISED)
btn_save = tk.Button(fr_buttons, text="Save As...", command=saveFiles)
btn_open = tk.Button(fr_buttons, text="Open", command=openFiles)
btn_style = tk.Button(fr_buttons, text="Poem Style", command=StyleIndentifier)
btn_rhyme_style = tk.Button(fr_buttons, text="Rhyme Style", command=RhymeStyleIdentifier)
btn_syllable = tk.Button(fr_buttons, text="Syllable Counter", command=SyllableCounter)
btn_rhyme = tk.Button(fr_buttons, text="Rhyming Words Finder", command=RhymeSuggestion)


#specifing position of buttons
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_open.grid(row=0, column=0, sticky="ew", padx=5)
btn_style.grid(row=2, column=0, sticky="ew", padx=5)
btn_syllable.grid(row=4, column=0, sticky="ew", padx=5)
btn_rhyme.grid(row=5, column=0, sticky="ew", padx=5)
btn_rhyme_style.grid(row=3, column=0, sticky="ew", padx=5)


#specifying position of button grid in overall display window
fr_buttons.grid(row=0, column=0, sticky="ns")

#specifying position of text box in overall display window
txt_edit.grid(row=0, column=1, sticky="nsew")

#running the display window
window.mainloop()