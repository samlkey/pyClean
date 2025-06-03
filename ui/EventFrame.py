from tkinter import ttk
from tkinter import *

class EventFrame:
    def __init__(self, root):
        self.root = root
        self.frame = None
        self.elements = {} 
        self.files_rendered = 0 
        self.row_index = 0  
    
    def show(self, c, r, w, h):
        w1 = LabelFrame(self.root)
        w1.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

        # Create canvas
        canvas = Canvas(w1, width=w, height=h)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Vertical scrollbar
        yscroll = ttk.Scrollbar(w1, orient=VERTICAL, command=canvas.yview)
        yscroll.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=yscroll.set)

        # Horizontal scrollbar
        xscroll = ttk.Scrollbar(w1, orient=HORIZONTAL, command=canvas.xview)
        xscroll.grid(row=1, column=0, sticky="ew")
        canvas.configure(xscrollcommand=xscroll.set)

        # Grid weight so the canvas resizes with the window/frame
        w1.rowconfigure(0, weight=1)
        w1.columnconfigure(0, weight=1)

        # Inner frame inside the canvas
        self.frame = Frame(canvas)
        self.frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.frame, anchor="nw")

    def insert(self, e, name, c, sticky=None):
        assert self.frame is not None, "show() EventFrame before inserting elements."
        e.grid(column=c, row=self.row_index, sticky=sticky)
        self.elements[name] = e
        self.row_index += 1

    def remove(self, name):
        widget = self.elements.get(name)
        if widget:
            widget.destroy()
            del self.elements[name]
            self.row_index -= 1
        else:
            print(f"Element '{name}' not found.")