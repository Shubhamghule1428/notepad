from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    sg.title("untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(
        defaultextension=".txt",
        filetypes=[("All files", "."), ("Text Document"), ("*.txt")],
    )

    if file == "":
        file = None
    else:
        sg.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(
            initialfile="untitled.txt",
            defaultextension=".txt",
            filetypes=[("All files", "."), ("Text Documents", "*.txt")],
        )

        if file == "":
            file = None

        else:

            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            sg.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "*")
        f.write(TextArea.get(1.0, END))


def quitApp():
    sg.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by Shubham Ghule")


if __name__ == "__main":
    sg = Tk()
    sg.title("untitled- Notepad")

    sg.geometry("644x788")

    TextArea = Text(sg, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    sg.mainloop()
