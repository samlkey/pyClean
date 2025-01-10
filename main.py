import tkinter
import sv_ttk

from cleanMethods import Run
from tkinter import filedialog
from tkinter import ttk
from tkinter import *

#folder selecter, with filters, run on right

def on_click():
    filename = filedialog.askdirectory()
    lbl.config(text=filename)

root = tkinter.Tk()
root.title("pyClean")
root.geometry("500x370")
root.resizable(height=FALSE, width=FALSE)

lbl = ttk.Label(root, background="white", foreground="black", font=("Arial", 14), text="")
lbl.config()
#lbl.grid(row=0, column=0)
btn = ttk.Button(root, text="Browse", command=on_click)

#Need to gather filters and send them over to Run
#lambda for gathering params
run = ttk.Button(root, text="Run", command=lambda: Run(params={
    "dir": lbl.cget("text"),
    "folder_filter": folder_int.get(),
    "size_filter": size_int.get(),
    "empty_filter": empty_int.get()
}))

#filters
folder_int = tkinter.IntVar()
folder_check = ttk.Checkbutton(root, text="Filter based on Format?", variable=folder_int)

size_int = tkinter.IntVar()
size_check = ttk.Checkbutton(root, text="Filter based on File Size?", variable=size_int)

empty_int = tkinter.IntVar()
empty_check = ttk.Checkbutton(root, text="Remove Empty Folders?", variable=empty_int)

btn.pack()
lbl.pack()
run.pack()
folder_check.pack()
size_check.pack()
empty_check.pack()

sv_ttk.set_theme("dark")

root.mainloop()
#dont forget to load the venv

#ttk vs tk
#https://stackoverflow.com/questions/19561727/what-is-the-difference-between-the-widgets-of-tkinter-and-tkinter-ttk-in-python