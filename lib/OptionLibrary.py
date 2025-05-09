import tkinter as tk

class OptionLibrary:
    def __init__(self):
        # Options
        self.options = {
            "Windows": {
                "Apps/Programs": tk.IntVar(),
                "Compressed Files": tk.IntVar(),
                "Pictures/Images": tk.IntVar(),
                "Audio/Video": tk.IntVar(),
                "Documents": tk.IntVar()
            },
            "Internet Explorer": {
                "Clear Cache": tk.IntVar(),
                "Temporary Internet Files": tk.IntVar(),
                "Clear Cookies": tk.IntVar(),
                "Saved Passwords": tk.IntVar(),
                "Delete Browsing History": tk.IntVar()
            },
            "Downloads": {
                "Apps/Programs": tk.IntVar(),
                "Compressed Files": tk.IntVar(),
                "Pictures/Images": tk.IntVar(),
                "Audio/Video": tk.IntVar(),
                "Documents": tk.IntVar()
            }
        }
    
    def get_sel_options(self):
        sel = [] 
        for category, options in self.options.items():
            for name, var in options.items():
                if(var.get() == 1): sel.append(name)

        return sel 

