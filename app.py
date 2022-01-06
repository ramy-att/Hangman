#!/usr/bin/env python3.10

import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import Cover, Game

# ~ #Crispy Text
# ~ try:
    # ~ from ctypes import windll
    # ~ windll.shcore.SetProcessDpiAwareness(1)
# ~ except:
    # ~ pass

class Hangman(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hangman Game")
        self.geometry("500x700")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.frames= dict()
        cover_frame = Cover(self)
        cover_frame.grid(row=0, column=0, sticky="NSEW")

        game_frame= Game(self)
        game_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Cover]=cover_frame
        self.frames[Game]=game_frame

        self.show_frame(Cover)

    def show_frame(self,containter):
        frame= self.frames[containter]
        frame.tkraise()

def main():
    app = Hangman()
    app.resizable(False, False)

    style= ttk.Style(app)
    font.nametofont("TkDefaultFont").configure(
        family= "Comic Sans MS",
        size=12
    )
    app.mainloop()

if __name__ == '__main__':
    main()
