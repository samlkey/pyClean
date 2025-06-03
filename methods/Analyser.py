from pathlib import Path
from lib import ExtensionLibrary
from tkinter import messagebox

import os

class Analyser:
    def __init__(self, prog):
        self.progress = prog
        self.extensions = ExtensionLibrary().extensions
        
        self.analyse_info = {
            "Total Files": 0,
            "Size": 0,
            #make this a map, then map each option
            "Files": {},
            "Option Size": {}
        }

        self.progress["value"] = 0
        
        self.actions = {
            "Desktop": lambda: self.directory_clean("Desktop"),
            "Documents": lambda: self.directory_clean("Documents", "Documents"),
            "Downloads": lambda: self.directory_clean("Downloads"),
            "Music": lambda: self.directory_clean("Music", "Audio/Video"),
            "Pictures/Images": lambda: self.directory_clean("Pictures", "Pictures/Images"),
            "Audio/Video": lambda: self.directory_clean("Videos", "Audio/Video")    
        }

    def analyse(self, ol):
        self.progress["value"] = 0
        sel = ol.get_sel_options()

        if len(sel) == 0:
            messagebox.showerror("Error", "Please select options before analysing!")
            return

        for cmd in sel:
            self.actions.get(cmd, self.unknown)()

        self.progress["value"] = 100
        return self.analyse_info


    #directory based 
    #for cleans targetting a specfic directory plus extension combo

    def directory_clean(self, filePath, extension=None):
        doc_path = Path.home() / filePath

        self.progress["value"] = 25
        # self.progress_lbl.config(text="25%")

        if extension == None:
            tbl = [str(file) for file in doc_path.iterdir()]
        else:
            document_extensions = self.extensions[extension]

            tbl = [str(file) for file in doc_path.iterdir()
            if file.is_file() and file.suffix.lower() in document_extensions]

        self.update_analyse_data(tbl, filePath)

    def update_analyse_data(self, files, filePath):
        self.progress["value"] = 50
        option_size = 0

        for file in files:
            self.analyse_info["Size"] += os.path.getsize(file)
            option_size += os.path.getsize(file)
            self.analyse_info["Total Files"] += 1
            
            #Find map for curr dir 
            if filePath not in self.analyse_info["Files"]:
                self.analyse_info["Files"][filePath] = []
            else:
                self.analyse_info["Files"][filePath].append(str(file))

        self.analyse_info["Option Size"][filePath] = option_size; 

    def downloads():
        print("down")

    def unknown(self):
        print("Error: Unknown cmd")


