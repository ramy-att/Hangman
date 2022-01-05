import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class Cover(ttk.Frame):
    def __init__(self,parent, show_game):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.cover_frame = ttk.Frame(self)
        self.cover_frame.grid(row=0, column=0, sticky="NSEW")

        #COVER PAGE

        cover_image = Image.open("./assets/Hangman.png")
        cover_photo = ImageTk.PhotoImage(cover_image)

        cover_label = tk.Label(
            self.cover_frame ,
            image=cover_photo
        )

        cover_label.image = cover_photo
        cover_label.grid(
            row=0,
            column=0,
            sticky="NEW"
        )
        #Play button -cover page

        play_button= ttk.Button(
            self.cover_frame,
            text="Play",
            command=show_game
        )

        play_button.grid(
            row=1,
            column=0,
            sticky= "SEW",
            pady=(10,10),
            padx=(10,10),
        )

class Game(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chances=0
        self.underscore_list = []
        self.pos=0
        self.entered_val = tk.StringVar()
        self.message=tk.StringVar()
        self.message.set("Use keyboard")

        fp = open("./assets/hangman_words.txt")
        self.lst = fp.readlines()
        for x in range(len(self.lst)):
            self.lst[x] = self.lst[x].rstrip('\n').lower()

        def get_word():
            self.word = random.choice(self.lst)
            print(self.word)
            print(self.underscore_list)
            for char in self.word:
                self.underscore_list.append("_")

        photos=["./assets/1.png","./assets/2.png","./assets/3.png","./assets/4.png","./assets/5.png","./assets/6.png","./assets/7.png","./assets/8.png"]

        self.playing_frame= ttk.Frame(self)
        self.playing_frame.grid(row=0, column=0, sticky="NSEW")
        welcome_label= ttk.Label(
            self.playing_frame,
            textvariable=self.message
        )
        welcome_label.place(relx=0.5, rely=0.1, anchor="center")


        def put_char(WordList):
            pos = 0
            for char in WordList:
                character=ttk.Label(
                    self.playing_frame,
                    text=str(char)
                )
                character.place(rely=0.8,relx=0.2+pos, anchor="center")
                pos+=0.05

        def put_image(image_name):
            image = Image.open(str(image_name))
            photo = ImageTk.PhotoImage(image)

            img_label = tk.Label(
                self.playing_frame,
                image=photo
            )
            img_label.image = photo
            img_label.place(
                relx=0.2,
                rely=0.15,
            )

        get_word()

        put_char(self.underscore_list)
        put_image(photos[0])

        def submit():
            self.game_started=False
            if self.entered_val.get() in self.word and self.entered_val.get() not in self.underscore_list:
                for i in range(len(self.word)):
                    if self.word[i]==self.entered_val.get():
                        self.underscore_list[i]=self.entered_val.get()
                        put_char(self.underscore_list)
                        print(self.underscore_list)
            else:
                try:
                    self.chances+=1
                    if self.chances==7:
                        self.game_lost = True
                        self.message.set("You suck!")
                        put_image(photos[self.chances])
                        put_char(list(self.word))
                    else:
                        put_image(photos[self.chances])
                except:
                    pass

            if "_" not in self.underscore_list:
                self.message.set("Siu")

            self.e1.delete(first=0)

        def reset():
            self.underscore_list.clear()
            self.message.set("Use keyboard")
            self.chances = 0
            self.entered_val.set("")
            get_word()
            put_char(self.underscore_list)
            put_image(photos[0])
            print(self.underscore_list)

        self.e1 = tk.Entry(self.playing_frame, textvariable=self.entered_val)
        self.e1.place(rely=0.9, relx=0.5, anchor="center")
        submit_button = tk.Button(self.playing_frame,
                            text='Submit',
                            fg='White',
                            bg='dark green',
                            command= submit
                        )
        submit_button.place(rely=0.96, relx=0.5, anchor="center")

        reset_button = tk.Button(self.playing_frame,
                                    text='Reset',
                                    fg='White',
                                    bg='red',
                                    command=reset,
                                  )
        reset_button.grid(padx= 10,pady=10)

class GameOver(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.game_over_frame = ttk.Frame(self)
        self.game_over_frame.grid(row=0, column=0, sticky="NSEW")

        photo= "./assets/gameover.png"

        image = Image.open(str(photo))
        photo = ImageTk.PhotoImage(image)

        img_label = tk.Label(
            self.game_over_frame,
            image=photo
        )
        img_label.image = photo
        img_label.place(
            relx=0.2,
            rely=0.15,
        )
