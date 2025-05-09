#dependencies
import tkinter as tk

from ui import ScrollableFrame, EventFrame
from lib import FontLibrary, OptionLibrary
from methods import Analyser

from tkinter import filedialog
from tkinter import ttk
from tkinter import *

def main():
    root = tk.Tk()
    root.title("pyClean")
    root.geometry("1000x370")
    root.resizable(height=FALSE, width=FALSE)

    # Font 
    fonts = FontLibrary()

    # Force geometry update
    root.update_idletasks()

    # Options ----------------------------------

    ol = OptionLibrary()

    sf = ScrollableFrame(root)
    sf.show(0, 0, (root.winfo_width() // 2) - 25, root.winfo_height() - 30) 

    i = 1
    for category, options in ol.options.items():
        sf.insert(Label(sf.frame, text=category, font=fonts.get("heading"), padx=10, pady=10), 0, i)
        i += 1
        for name, var in options.items():
            sf.insert(Checkbutton(sf.frame, text=name, font=fonts.get("option"), variable=var), 1, i)
            i += 1

    #Event Frame --------------------------------

    ev = EventFrame(root)
    ev.show(1, 0, (root.winfo_width() // 2) - 50, root.winfo_height() - 30)
    
    ev.insert(ttk.Progressbar(ev.frame, orient="horizontal", length=400, mode="determinate", ), "prog_bar", 0, 0, "nw")
    ev.insert(Label(ev.frame, text="0%", font=fonts.get("bold"), padx=10), "prog_lbl", 1, 0, "nw")

    ev.insert(Button(ev.frame, text="Analyse", width=17, command=lambda: run_analyse(ol, ev)), "analyse_btn", 0, 1, "nw")
    ev.insert(Button(ev.frame, text="Run", width=17), "run_btn", 0, 1)

    ev.insert(Label(ev.frame, text="", font=fonts.get("bold")), "filler", 0, 3, "nw")

    ev.insert(Label(ev.frame, text="Total Files: 0", font=fonts.get("bold")), "file_lbl", 0, 4, "nw")
    ev.insert(Label(ev.frame, text="Size: 0KB", font=fonts.get("bold")), "size_lbl", 0, 5, "nw")
    ev.insert(Label(ev.frame, text="Files:", font=fonts.get("bold")), "fileid_lbl", 0, 6, "nw")

    # -------------------------------------------

    root.mainloop()

def run_analyse(ol, ev):
    # RESET LABELS THROUGH EVENT FRAME

    ev.elements["file_lbl"].config(text="Total Files: 0")
    ev.elements["size_lbl"].config(text="Size: 0KB")


    ayl = Analyser(ev.elements["prog_bar"], ev.elements["prog_lbl"])
    
    info = ayl.analyse(ol)
    print(info)

    if info == None:
        return
    
    # UPDATE LABELS THROUGH EVENT FRAME

    ev.elements["file_lbl"].config(text=f"Total Files: {str(info["Total Files"])}")
    ev.elements["size_lbl"].config(text=f"Size: {str(info["Size"])}KB")

    # Font 
    fonts = FontLibrary()
    i = 1

    for file in info["Files"]:
        var = IntVar
        ev.insert(Checkbutton(ev.frame, text=file, font=fonts.get("bold"), padx=15, variable=var), f"filelst_lbl{i}", 0, i+6, "nw")
        i += 1
        

main()
#dont forget to load the venv

#ttk vs tk
#https://stackoverflow.com/questions/19561727/what-is-the-difference-between-the-widgets-of-tkinter-and-tkinter-ttk-in-python

#make this a class mayb? so I can update progress bar without having to pass it through