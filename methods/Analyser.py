from pathlib import Path
from lib import ExtensionLibrary
from tkinter import messagebox

import os

class Analyser:
    def __init__(self, prog, prog_lbl):
        self.progress = prog
        self.progress_lbl = prog_lbl
        self.extensions = ExtensionLibrary().extensions
        self.actions = {
            "Documents": self.docs
        }
        self.analyse_info = {
            "Total Files": 0,
            "Size": 0,
            "Files": []
        }

        self.progress["value"] = 0
        self.progress_lbl.config(text="0%")

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

    def docs(self):
        document_extensions = self.extensions["Documents"]
        doc_path = Path.home() / "Documents"

        self.progress["value"] = 25
        self.progress_lbl.config(text="25%")
        #-- Might be able to be refactored into a func ----------------

        doc_files = [
            str(file) for file in doc_path.iterdir()
            if file.is_file() and file.suffix.lower() in document_extensions
        ]

        self.progress["value"] = 50
        self.progress_lbl.config(text="50%")

        # UPDATE ANALYSE INFO -------------------------------------
        for file in doc_files:
            self.analyse_info["Size"] += round(os.path.getsize(file) / 1024, 1) #KB
            self.analyse_info["Total Files"] += 1
            self.analyse_info["Files"].append(str(file))

        #----------------------------------------------------------------

    def downloads():
        print("down")





    def unknown(self):
        print("Error: Unknown cmd")


