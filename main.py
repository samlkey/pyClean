#dependencies
import tkinter as tk

from ui import ScrollableFrame, EventFrame
from lib import FontLibrary, OptionLibrary
from methods import Analyser

from tkinter import ttk
from tkinter import *

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.fl = FontLibrary()
        self.ol = OptionLibrary()
        self.ev = EventFrame(self.root)

        self.root.title("pyClean")
        self.root.geometry("1200x400")
        self.root.resizable(height=FALSE, width=FALSE)
        self.root.update_idletasks()

    def show(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Options", command=self.option_menu)

        menubar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menubar)
        sf = ScrollableFrame(self.root)
        sf.show(0, 0, (self.root.winfo_width() // 2) - 25, self.root.winfo_height() - 30) 

        i = 1
        for category, options in self.ol.options.items():
            sf.insert(Label(sf.frame, text=category, font=self.fl.get("heading"), padx=10, pady=10), 0, i)
            i += 1
            for name, var in options.items():
                sf.insert(Checkbutton(sf.frame, text=name, font=self.fl.get("option"), variable=var), 1, i)
                i += 1
        
        #Event Frame ----------------------------------

        self.ev.show(1, 0, (self.root.winfo_width() // 2) - 70, self.root.winfo_height() - 50)      
        self.ev.insert(ttk.Progressbar(self.ev.frame, orient="horizontal", length=400, mode="determinate", ), "prog_bar", 0, 0, "nw")
        self.ev.insert(Button(self.ev.frame, text="Analyse", width=17, command=lambda: self.run_analyse()), "analyse_btn", 0, 1, "nw")
        # self.ev.insert(Button(self.ev.frame, text="Run", width=17), "run_btn", 0, 1)   
        # self.ev.insert(Label(self.ev.frame, text="", font=self.fl.get("bold")), "filler", 0, 3, "nw")   
        self.ev.insert(Label(self.ev.frame, text="Total Files: 0", font=self.fl.get("bold")), "file_lbl", 0, 2, "nw")
        self.ev.insert(Label(self.ev.frame, text="Size: 0KB", font=self.fl.get("bold")), "size_lbl", 0, 3, "nw")

        # ---------------------------------------------

        self.root.mainloop()

    def run_analyse(self):
        # CLEAR LABELS FROM FILES: 
        for i in range(self.ev.files_rendered):
            self.ev.remove(f"filelst_lbl{i}")

        self.ev.files_rendered = 0 

        # RESET LABELS THROUGH EVENT FRAME
        self.ev.elements["file_lbl"].config(text="Total Files: 0")
        self.ev.elements["size_lbl"].config(text="Size: 0")

        ayl = Analyser(self.ev.elements["prog_bar"])
        info = ayl.analyse(self.ol)

        if info == None:
            return
        
        print(info["Option Size"])
        self.update_information(info)

        
    def update_information(self, info):
        # # UPDATE LABELS THROUGH EVENT FRAME
        self.ev.elements["file_lbl"].config(text=f"Total Files: {str(info["Total Files"])}")
        

        self.ev.elements["size_lbl"].config(text=f"Size: {self.convert_size(info["Size"])}")

        # Font
        fonts = FontLibrary()

        i = 0
        for key, value in info["Option Size"].items():
            self.ev.insert(Label(self.ev.frame, text=f"{key} Total: {self.convert_size(value)}", font=self.fl.get("bold")), f"filelst_lbl{i}", 0, i+6, "nw")
            i += 1
            self.ev.files_rendered += 1

        for file in info["Files"]:
            var = IntVar
            self.ev.insert(Checkbutton(self.ev.frame, text=file, font=fonts.get("bold"), padx=15, variable=var), f"filelst_lbl{i}", 0, i+6, "nw")
            i += 1
            self.ev.files_rendered += 1

    def convert_size(self, input_size):
        size = ""

        if input_size < 1024:
            # KB (less than 1KB)
            size = f"{input_size:.2f} KB"
        elif input_size < 1048576:
            # MB (between 1KB and 1MB)
            size = f"{input_size:.2f} KB"
        elif input_size < 1073741824:
            # GB (between 1MB and 1GB)
            size= f"{input_size / (1024 * 1024):.2f} MB"
        else:
            # GB for sizes greater than 1GB
            size = f"{input_size / (1024 ** 3):.2f} GB"

        return size



    def option_menu(self):
        print("Options clicked")


if __name__ == "__main__":
    app = MainWindow()
    app.show()

#To do,
#Adding "SETTINGS" to change stuff like the ExtensionLibrary
#Directory break down on "Files:"

#ttk vs tk
#https://stackoverflow.com/questions/19561727/what-is-the-difference-between-the-widgets-of-tkinter-and-tkinter-ttk-in-python

#make this a class mayb? so I can update progress bar without having to pass it through