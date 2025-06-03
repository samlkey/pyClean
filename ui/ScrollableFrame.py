import tkinter as tk

from tkinter import ttk
from tkinter import *

class ScrollableFrame:
    def __init__(self, root):
        self.root = root
        self.frame = None
        
    def show(self, c, r, w, h, bg='#2D2D2D'):
        # Modern container frame
        container = Frame(self.root, bg=bg)
        container.grid(row=r, column=c, sticky="nsew", padx=10, pady=10)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Modern canvas with custom styling
        canvas = Canvas(container, 
                      width=w, 
                      height=h,
                      bg=bg,
                      highlightthickness=0,  # Remove border
                      bd=0)  # Remove border
        canvas.grid(row=0, column=0, sticky="nsew")

        # Modern scrollbar
        style = ttk.Style()
        style.configure("Modern.Vertical.TScrollbar",
                      background=bg,
                      troughcolor='#363636',
                      width=10,
                      arrowcolor='#FFFFFF')

        scrollbar = ttk.Scrollbar(container,
                                orient=VERTICAL,
                                command=canvas.yview,
                                style="Modern.Vertical.TScrollbar")
        scrollbar.grid(row=0, column=1, sticky="ns", padx=(2, 0))

        # Configure canvas scrolling
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # Inner frame for content
        self.frame = Frame(canvas, bg=bg)
        canvas.create_window((0, 0), window=self.frame, anchor="nw", width=w-20)  # Adjust width for scrollbar

        # Configure mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        # Bind mouse wheel to both canvas and frame
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        self.frame.bind_all("<MouseWheel>", _on_mousewheel)

    def insert(self, widget, col, row, sticky="w", padx=0, pady=0):
        """Insert a widget with modern styling"""
        assert self.frame is not None, "Call show() before inserting elements."
        widget.grid(column=col, row=row, sticky=sticky, padx=padx, pady=pady)