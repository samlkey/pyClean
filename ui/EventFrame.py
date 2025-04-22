from tkinter import ttk
from tkinter import *

class EventFrame:
    def __init__(self, root):
        self.root = root
        self.frame = None
    
    def show(self, c, r, w, h):
        w1 = LabelFrame(self.root)
        w1.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
        canvas = Canvas(w1, width=w, height=h)
        canvas.grid(row=0, column=1, sticky="nsew")

        self.frame = Frame(canvas)
        canvas.create_window((0, 0), window=self.frame, anchor="nw")

    def insert(self, e, c, r, sticky):
        assert self.frame is not None, "show() EventFrame before inserting elements."
        e.grid(column=c, row=r, sticky=sticky)