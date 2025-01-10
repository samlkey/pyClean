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
    "type_filter": selected_option.get(),
    "empty_filter": empty_int.get(),
    "recursive_filter": recursive_int.get() 
}))

#filters radio
selected_option = tkinter.StringVar(value="Filter based on Format?")
folder_check = ttk.Radiobutton(root, text="Filter based on Format?", value="type", variable=selected_option)
size_check = ttk.Radiobutton(root, text="Filter based on File Size?", value="size", variable=selected_option)

#filters check
empty_int = tkinter.IntVar()
empty_check = ttk.Checkbutton(root, text="Remove Empty Folders?", variable=empty_int)

recursive_int = tkinter.IntVar()
recursive_check = ttk.Checkbutton(root, text="Recursive?", variable=recursive_int)

btn.pack(pady=15)
lbl.pack(pady=15)

folder_check.pack()
size_check.pack()

empty_check.pack()
recursive_check.pack()

run.pack(pady=15)

sv_ttk.set_theme("dark")

root.mainloop()
#dont forget to load the venv

#ttk vs tk
#https://stackoverflow.com/questions/19561727/what-is-the-difference-between-the-widgets-of-tkinter-and-tkinter-ttk-in-python