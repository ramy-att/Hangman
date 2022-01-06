import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class Cover(ttk.Frame):
    def __init__(self,parent):
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
            command= lambda: parent.show_frame(Game)
        )

        play_button.grid(
            row=1,
            column=0,
            sticky= "SEW",
            pady=(10,10),
            padx=(10,10),
        )

photos=["./assets/1.png","./assets/2.png","./assets/3.png","./assets/4.png","./assets/5.png","./assets/6.png","./assets/7.png","./assets/8.png"]
class Game(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        fp = open("./assets/hangman_words.txt")
        self.lst = fp.readlines()
        for x in range(len(self.lst)):
            self.lst[x] = self.lst[x].rstrip('\n').lower()

        self.entered_val = tk.StringVar()
        self.message=tk.StringVar()

        self.playing_frame= ttk.Frame(self)
        self.playing_frame.grid(row=0, column=0, sticky="NSEW")
        welcome_label= ttk.Label(
            self.playing_frame,
            textvariable=self.message
        )
        welcome_label.place(relx=0.5, rely=0.1, anchor="center")

        self.e1 = tk.Entry(self.playing_frame, textvariable=self.entered_val)
        self.e1.place(rely=0.85, relx=0.5, anchor="center")

        submit_button = tk.Button(self.playing_frame,
                            text='Submit',
                            fg='White',
                            bg='green',
                            command=self.submit
                        )
        submit_button.place(rely=0.96, relx=0.5, anchor="center")

        reset_button = tk.Button(self.playing_frame,
                                    text='Reset',
                                    fg='White',
                                    bg='red',
                                    command=self.reset,
                                  )
        reset_button.grid(padx= 10,pady=10)

        submit_button.bind("<Enter>", self.on_enter)
        submit_button.bind("<Leave>", self.on_leave)
        reset_button.bind("<Enter>", self.on_enter_2)
        reset_button.bind("<Leave>", self.on_leave_2)

        self.reset_game()

    def reset_game(self):
        self.chances=0
        self.underscore_list = []
        self.pos=0

        self.message.set("Use keyboard")
        self.get_word()
        self.put_char(self.underscore_list)
        self.put_image(photos[0])

    def get_word(self):
        self.word = random.choice(self.lst)
        print(self.word)
        print(self.underscore_list)
        for char in self.word:
            self.underscore_list.append("_")

    def put_char(self, WordList):
        pos = 0
        for char in WordList:
            character=ttk.Label(
                self.playing_frame,
                text=char
            )
            character.place(rely=0.75,relx=0.2+pos, anchor="center")
            pos+=0.05

    def put_image(self, image_name):
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

    def submit(self):
        self.game_started=False
        if self.entered_val.get() in self.word and self.entered_val.get() not in self.underscore_list:
            for i in range(len(self.word)):
                if self.word[i]==self.entered_val.get():
                    self.underscore_list[i]=self.entered_val.get()
                    self.put_char(self.underscore_list)
                    print(self.underscore_list)
        else:
            try:
                self.chances+=1
                if self.chances==7:
                    self.game_lost = True
                    self.message.set("You suck!")
                    self.put_image(photos[self.chances])
                    self.put_char(list(self.word))
                else:
                    self.put_image(photos[self.chances])
            except:
                pass

        if "_" not in self.underscore_list:
            self.message.set("Siu")

        self.e1.delete(first=0)

    def reset(self):
        reset_game()

    def on_enter(self, e):
        e.widget['background'] = 'green'

    def on_leave(self, e):
        e.widget['background'] = 'dark green'

    def on_leave_2(self, e):
        e.widget['background'] = 'red'

    def on_enter_2(self, e):
        e.widget['background'] = 'pale violet red'

