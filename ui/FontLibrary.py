import tkinter.font as tkFont

class FontLibrary:
    def __init__(self, root):
        self.root = root
        self.fonts = {
            "heading": tkFont.Font(size=14, weight="bold", slant="italic"),
            "option": tkFont.Font(size=10, weight="bold", slant="italic"),
            "bold": tkFont.Font(size=10, weight="bold")
        }
    
    def get(self, key):
        return self.fonts.get(key)