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