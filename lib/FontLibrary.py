import tkinter.font as tkFont

class FontLibrary:
    def __init__(self):
        self.fonts = {
            "heading": tkFont.Font(size=14, weight="bold"),
            "option": tkFont.Font(size=10, weight="bold", slant="italic"),
            "bold": tkFont.Font(size=10, weight="bold")
        }
    
    def get(self, key):
        return self.fonts.get(key)