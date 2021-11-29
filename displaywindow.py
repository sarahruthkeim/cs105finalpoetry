import tkinter as tk


window = tk.Tk()
window.title("Poems")
window.geometry("800x100")


sample_text = tk.Entry(window)
sample_text.pack()


def set_text_by_button():

    sample_text.delete(0, "end")

    sample_text.insert(0, "Poem Saved")

set_up_button = tk.Button(window, height=1, width=10, text="Save",
                               command=set_text_by_button)

set_up_button.pack()

window.mainloop()


