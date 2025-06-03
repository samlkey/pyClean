#dependencies
import tkinter as tk
from tkinter import ttk
from tkinter import *

from ui import ScrollableFrame, EventFrame
from lib import FontLibrary, OptionLibrary
from methods import Analyser

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.fl = FontLibrary()
        self.ol = OptionLibrary()
        self.ev = EventFrame(self.root)

        # Configure main window
        self.root.title("pyClean")
        self.root.geometry("1200x700")  # Larger default size
        self.root.configure(bg='#1E1E1E')  # Dark background
        self.root.resizable(False, False)  # Make window non-resizable
        
        # Configure modern styles
        self.style = ttk.Style()
        self.style.configure("Modern.TButton",
                           font=('Segoe UI', 11),
                           background='#007AFF',
                           foreground='#FFFFFF',
                           padding=10)

        self.root.update_idletasks()

    def show(self):
        # Modern menubar
        menubar = tk.Menu(self.root, bg='#2D2D2D', fg='#FFFFFF', relief=FLAT)
        file_menu = tk.Menu(menubar, tearoff=0, bg='#2D2D2D', fg='#FFFFFF')
        file_menu.add_command(label="Options", command=self.option_menu)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

        # Main container frame
        frame = Frame(self.root, bg='#1E1E1E')
        frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

        # Center content frame with modern card-like appearance
        content = Frame(frame, bg='#2D2D2D', padx=40, pady=40)
        content.grid(row=0, column=0)

        # App title/logo
        Label(content,
              text="pyClean",
              font=('Segoe UI', 32, 'bold'),
              bg='#2D2D2D',
              fg='#FFFFFF').grid(row=0, column=0, sticky="w", pady=(0, 20))

        # Subtitle
        Label(content,
              text="System Cleanup Utility",
              font=('Segoe UI', 14),
              bg='#2D2D2D',
              fg='#888888').grid(row=1, column=0, sticky="w", pady=(0, 30))

        # Disclaimer sections
        disclaimers = [
            ("Purpose", "This program is designed to clean up your system by removing selected files."),
            ("Safety", "Only safe-to-delete files will be included. System files are automatically excluded."),
            ("Disclaimer", "The developer is not responsible for any information lost as a result of using this program.")
        ]

        for i, (title, text) in enumerate(disclaimers):
            # Section title
            Label(content,
                  text=title,
                  font=('Segoe UI', 12, 'bold'),
                  bg='#2D2D2D',
                  fg='#007AFF').grid(row=i*2 + 2, column=0, sticky="w", pady=(20, 5))
            
            # Section content
            Label(content,
                  text=text,
                  font=('Segoe UI', 11),
                  bg='#2D2D2D',
                  fg='#FFFFFF',
                  wraplength=600,
                  justify="left").grid(row=i*2 + 3, column=0, sticky="w")

        # Spacer
        Frame(content, height=20, bg='#2D2D2D').grid(row=8, column=0)

        # Agreement button with modern styling
        btn = Button(content,
                    text="I Understand and Agree",
                    font=('Segoe UI', 11, 'bold'),
                    bg='#007AFF',
                    fg='#FFFFFF',
                    activebackground='#0051A8',
                    activeforeground='#FFFFFF',
                    relief=FLAT,
                    padx=30,
                    pady=12,
                    cursor="hand2",
                    command=lambda: self.main_menu(content))
        btn.grid(row=9, column=0, sticky="e", pady=(20, 0))

        self.root.mainloop()

    def main_menu(self, *args):
        for widget in args:
            widget.grid_forget()

        sf = ScrollableFrame(self.root)
        sf.show(0, 0, (self.root.winfo_width() // 2) - 25, self.root.winfo_height() - 30) 

        i = 1
        for category, options in self.ol.options.items():
            sf.insert(Label(sf.frame, text=category, font=self.fl.get("heading"), padx=10, pady=10, bg='#2D2D2D', fg='#FFFFFF'), 0, i)
            i += 1
            for name, var in options.items():
                sf.insert(Checkbutton(sf.frame, text=name, font=self.fl.get("option"), variable=var, 
                                    bg='#2D2D2D', fg='#FFFFFF', selectcolor='#2D2D2D', activebackground='#2D2D2D', activeforeground='#FFFFFF'), 1, i)
                i += 1
        
        #Event Frame ----------------------------------

        self.ev.show(1, 0, (self.root.winfo_width() // 2) - 70, self.root.winfo_height() - 50)      
        self.ev.insert(ttk.Progressbar(self.ev.frame, orient="horizontal", length=400, mode="determinate"), "prog_bar", 0, "nw")
        self.ev.insert(Button(self.ev.frame, text="Analyse", width=17, command=lambda: self.run_analyse()), "analyse_btn", 0, "nw")
        self.ev.insert(Label(self.ev.frame, text="Total Files: 0", font=self.fl.get("bold")), "file_lbl", 0, "nw")
        self.ev.insert(Label(self.ev.frame, text="Size: 0KB", font=self.fl.get("bold")), "size_lbl", 0, "nw")

        # ---------------------------------------------

    def run_analyse(self):
        # CLEAR LABELS FROM FILES: 
        for i in range(self.ev.files_rendered):
            self.ev.remove(f"filelst_lbl{i}")

        self.ev.files_rendered = 0 

        # RESET LABELS THROUGH EVENT FRAME
        self.ev.elements["file_lbl"].config(text="Total Files: 0")
        self.ev.elements["size_lbl"].config(text="Size: 0")

        ayl = Analyser(self.ev.elements["prog_bar"])
        info = ayl.analyse(self.ol)

        if info == None:
            return
        
        print(info["Files"])
        print(info["Option Size"])
        self.update_information(info)

        
    def update_information(self, info):
        # # UPDATE LABELS THROUGH EVENT FRAME
        self.ev.elements["file_lbl"].config(text=f"Total Files: {str(info["Total Files"])}")
        

        self.ev.elements["size_lbl"].config(text=f"Size: {self.convert_size(info["Size"])}")

        # Font
        fonts = FontLibrary()

        i = 0
        for key, value in info["Option Size"].items():
            self.ev.insert(Label(self.ev.frame, text=f"{key} Total: {self.convert_size(value)}", font=self.fl.get("bold")), f"filelst_lbl{i}", 0, "nw")
            i += 1
            self.ev.files_rendered += 1

        for key in info["Files"]:
            var = IntVar
            self.ev.insert(Checkbutton(self.ev.frame, text=key, font=fonts.get("bold"), variable=var), f"filelst_lbl{i}", 0, "nw")
            i += 1
            self.ev.files_rendered += 1

            for file in info["Files"][key]:
                var = IntVar
                self.ev.insert(Checkbutton(self.ev.frame, text=file, font=fonts.get("bold"), padx=15, variable=var), f"filelst_lbl{i}", 0, "nw")
                i += 1
                self.ev.files_rendered += 1


    def convert_size(self, input_size):
        size = ""
        if input_size < 1024:
            # KB (less than 1KB)
            size = f"{input_size:.2f} KB"
        elif input_size < 1048576:
            # MB (between 1KB and 1MB)
            size = f"{input_size:.2f} KB"
        elif input_size < 1073741824:
            # GB (between 1MB and 1GB)
            size= f"{input_size / (1024 * 1024):.2f} MB"
        else:
            # GB for sizes greater than 1GB
            size = f"{input_size / (1024 ** 3):.2f} GB"

        return size

    def option_menu(self):
        print("Options clicked")


if __name__ == "__main__":
    app = MainWindow()
    app.show()


#TODO,
#Adding "SETTINGS" to change stuff like the ExtensionLibrary
#indexes for rendering elements, like col and row should be handled by the ScrollableFrame and EventFrame objects
#Key buttons need to select the whole section

#BUG,
#Files is picking up folders, need to think of a way of handling folders (recursion)
