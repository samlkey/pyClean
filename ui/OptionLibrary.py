import tkinter as tk

class OptionLibrary:
    def __init__(self):
        
        # Options

        self.sys_opt = {
            "Empty Recycle Bin": tk.IntVar(),
            "Memory Dumps": tk.IntVar(),
            "Windows Log Files": tk.IntVar(),
            "Clipboard": tk.IntVar(),
            "Start Menu Shortcuts": tk.IntVar(),
            "Desktop Shortcuts": tk.IntVar()
        }

        self.ie_opt = {
            "Clear Cache": tk.IntVar(),
            "Temporary Internet Files": tk.IntVar(),
            "Clear Cookies": tk.IntVar(),
            "Saved Passwords": tk.IntVar(),
            "Delete Browsing History": tk.IntVar()
        }

        self.dw_opt = {
            "Apps/Programs": tk.IntVar(),
            "Compressed Files": tk.IntVar(),
            "Pictures/Images": tk.IntVar(),
            "Audio/Video": tk.IntVar(),
            "Documents": tk.IntVar()
        }