import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from poetrystyles import poem_type

def saveFiles():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt")],)
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)

def openFiles():
    filepath=tk.filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text files","*.txt*")],)
    with open(filepath, "r") as input_file:
        text=input_file.read()
        txt_edit.insert(tk.END, text)

window = tk.Tk()
window.title("Poem Analyzer")

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED)
btn_save = tk.Button(fr_buttons, text="Save As...", command=saveFiles)
btn_open = tk.Button(fr_buttons, text="Open", command=openFiles)
btn_style = tk.Button(fr_buttons, text="Poetry Style", command=poem_type())

btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_open.grid(row=0, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()
