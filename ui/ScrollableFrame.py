import tkinter as tk

from tkinter import ttk
from tkinter import *

class ScrollableFrame:
    def __init__(self, root):
        self.root = root
        self.frame = None
        
    def show(self, c, r, w, h):
        w1 = LabelFrame(self.root)
        w1.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

        # Configure the LabelFrame grid so contents can expand
        w1.grid_rowconfigure(0, weight=1)
        w1.grid_columnconfigure(0, weight=1)
        canvas = Canvas(w1, width=w, height=h)
        canvas.grid(row=r, column=c, sticky="nsew")
        yscroll = ttk.Scrollbar(w1, orient=VERTICAL, command=canvas.yview)
        yscroll.grid(row=r, column=c+1, sticky="ns")
        canvas.configure(yscrollcommand=yscroll.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))
        self.frame = Frame(canvas)
        # Optional: You may need to create a window inside the canvas to show the frame
        canvas.create_window((0, 0), window=self.frame, anchor="nw")
    
    def insert(self, e, c, r):
        assert self.frame is not None, "show() ScrollableFrame before inserting elements."
        e.grid(column=c, row=r, sticky="w")