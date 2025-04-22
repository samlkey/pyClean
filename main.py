#dependencies
import tkinter as tk
import tkinter.font as tkFont
import sv_ttk

from clean_methods import Run
from ui.ScrollableFrame import *
from ui.EventFrame import *
from ui.FontLibrary import *
from ui.OptionLibrary import *

from tkinter import filedialog
from tkinter import ttk
from tkinter import *

def main():
    root = tk.Tk()
    root.title("pyClean")
    root.geometry("1000x370")
    root.resizable(height=FALSE, width=FALSE)

    # Font 
    fonts = FontLibrary(root)

    # Force geometry update
    root.update_idletasks()

    # Options ----------------------------------
    ol = OptionLibrary()

    sf = ScrollableFrame(root)
    sf.show(0, 0, (root.winfo_width() // 2) - 25, root.winfo_height() - 30) 

    sf.insert(Label(sf.frame, text="Windows", font=fonts.get("heading"), padx=10, pady=10), 0, 0)

    i = 1
    for key, var in ol.sys_opt.items():
        sf.insert(Checkbutton(sf.frame, text=key, font=fonts.get("option"), variable=var), 1, i)
        i += 1

    sf.insert(Label(sf.frame, text="Internet Explorer", font=fonts.get("heading"), padx=10, pady=10), 0, i)
    i += 1
    for key, var in ol.ie_opt.items():
        sf.insert(Checkbutton(sf.frame, text=key, font=fonts.get("option"), variable=var), 1, i)
        i += 1

    sf.insert(Label(sf.frame, text="Windows Downloads", font=fonts.get("heading"), padx=10, pady=10), 0, i)
    i += 1
    for key, var in ol.dw_opt.items():
        sf.insert(Checkbutton(sf.frame, text=key, font=fonts.get("option"), variable=var), 1, i)
        i += 1

    #Event Frame --------------------------------

    ev = EventFrame(root)
    ev.show(1, 0, (root.winfo_width() // 2) - 50, root.winfo_height() - 30)
    
    ev.insert(ttk.Progressbar(ev.frame, orient="horizontal", length=400, mode="determinate"), 0, 0, "nw")
    ev.insert(Label(ev.frame, text="0%", font=fonts.get("bold"), padx=15), 1, 0, "nw")

    ev.insert(Button(ev.frame, text="Analyse", width=20), 0, 1, "nw")
    ev.insert(Button(ev.frame, text="Run", width=20), 0, 2, "nw")

    # -------------------------------------------

    # sv_ttk.set_theme("dark")
    root.mainloop()
    
main()
#dont forget to load the venv

#ttk vs tk
#https://stackoverflow.com/questions/19561727/what-is-the-difference-between-the-widgets-of-tkinter-and-tkinter-ttk-in-python




    # lbl = ttk.Label(root, background="white", foreground="black", font=("Arial", 14), text="")
    # lbl.config()
    # #lbl.grid(row=0, column=0)
    # btn = ttk.Button(root, text="Browse", command=lambda: on_click(lbl))

    # #Need to gather filters and send them over to Run
    # #lambda for gathering params
    # run = ttk.Button(root, text="Run", command=lambda: Run(params={
    #     "dir": lbl.cget("text"),
    #     "type_filter": selected_option.get(),
    #     "empty_filter": empty_int.get(),
    #     "recursive_filter": recursive_int.get() 
    # }))

    # #filters radio
    # selected_option = tkinter.StringVar(value="Filter based on Format")
    # folder_check = ttk.Radiobutton(root, text="Filter based on Format", value="type", variable=selected_option)

    # size_check = ttk.Radiobutton(root, text="Filter based on File Size", value="size", variable=selected_option)
    # size_textbox_min = ttk.Entry()
    # size_textbox_max = ttk.Entry()

    # #filters check
    # empty_int = tkinter.IntVar()
    # empty_check = ttk.Checkbutton(root, text="Remove Empty Folders", variable=empty_int)

    # recursive_int = tkinter.IntVar()
    # recursive_check = ttk.Checkbutton(root, text="Recursive", variable=recursive_int)

    # # btn.pack(pady=15)
    # # lbl.pack(pady=15)

    # # folder_check.pack()
    # # size_check.pack()
    # # size_textbox_min.pack()
    # # size_textbox_max.pack()

    # # empty_check.pack()
    # # recursive_check.pack()

    # # run.pack(pady=15)