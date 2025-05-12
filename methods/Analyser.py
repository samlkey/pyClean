from pathlib import Path
from lib import ExtensionLibrary
from tkinter import messagebox

import os

class Analyser:
    def __init__(self, prog, prog_lbl):
        self.progress = prog
        self.progress_lbl = prog_lbl
        self.extensions = ExtensionLibrary().extensions
        
        self.analyse_info = {
            "Total Files": 0,
            "Size": 0,
            "Files": []
        }

        self.progress["value"] = 0
        self.progress_lbl.config(text="0%")

        self.actions = {
            "Documents": lambda: self.directory_clean("Documents", "Documents"),
            "Pictures/Images": lambda: self.directory_clean("Pictures", "Pictures/Images")
        }

    def analyse(self, ol):
        sel = ol.get_sel_options()
        print(sel)

        if len(sel) == 0:
            messagebox.showerror("Error", "Please select options before analysing!")
            return

        for cmd in sel:
            self.actions.get(cmd, self.unknown)()

        self.progress["value"] = 100
        self.progress_lbl.config(text="100%")
        return self.analyse_info


    #directory based 
    #for cleans targetting a specfic directory plus extension combo

    def directory_clean(self, filePath, extension):
        document_extensions = self.extensions[extension]
        doc_path = Path.home() / filePath

        self.progress["value"] = 25
        self.progress_lbl.config(text="25%")

        self.update_analyse_data([
            str(file) for file in doc_path.iterdir()
            if file.is_file() and file.suffix.lower() in document_extensions
        ])

    def update_analyse_data(self, files):
        print(files)

        self.progress["value"] = 50
        self.progress_lbl.config(text="50%")

        for file in files:
            self.analyse_info["Size"] += round(os.path.getsize(file) / 1024, 1) #KB
            self.analyse_info["Total Files"] += 1
            self.analyse_info["Files"].append(str(file))



    def downloads():
        print("down")

    def unknown(self):
        print("Error: Unknown cmd")


