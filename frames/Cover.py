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

class ColorChangingButton(tk.Button):
    def __init__(self, master=None, hover_bg=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        if hover_bg is not None:
            self.bg_color = self['background']
            self.hover_bg = hover_bg
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
    def on_enter(self, e):
        self['background'] = self.hover_bg
    def on_leave(self, e):
        e.widget['background'] = self.bg_color

photos=["./assets/1.png","./assets/2.png","./assets/3.png","./assets/4.png","./assets/5.png","./assets/6.png","./assets/7.png","./assets/8.png"]
class Game(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        with open("./assets/hangman_words.txt") as fp:
            self.lst = fp.read().splitlines()

        self.entered_val = tk.StringVar()
        self.message=tk.StringVar()

        welcome_label= ttk.Label(
            self,
            textvariable=self.message
        )
        welcome_label.place(relx=0.5, rely=0.1, anchor="center")

        self.e1 = tk.Entry(self, textvariable=self.entered_val)
        self.e1.place(rely=0.85, relx=0.5, anchor="center")

        self.img_label = tk.Label(self)
        self.img_label.place(
            relx=0.2,
            rely=0.15,
        )

        submit_button = ColorChangingButton(self,
            text='Submit',
            fg='White',
            bg='green',
            hover_bg='dark green',
            command=self.submit
            )
        submit_button.place(rely=0.96, relx=0.5, anchor="center")

        reset_button = ColorChangingButton(self,
            text='Reset',
            fg='White',
            bg='red',
            hover_bg='pale violet red',
            command=self.reset_game,
            )
        reset_button.place(rely=0.1, relx=0.1)

        self.characters = tk.StringVar()
        charlbl=ttk.Label(self, textvariable=self.characters)
        charlbl.place(rely=0.75,relx=0.5, anchor="center")

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

    def put_char(self, word_list):
        self.characters.set(" ".join(word_list))

    def put_image(self, image_name):
        image = Image.open(str(image_name))
        photo = ImageTk.PhotoImage(image)
        self.img_label.config(image=photo)
        self.img_label.image = photo

    def submit(self):
        entered = self.entered_val.get()
        # todo: Add check if user entered non-character or more than 1 character
        if entered in self.word and entered not in self.underscore_list:
            for i, char in enumerate(self.word):
                if char == entered:
                    self.underscore_list[i]=entered
                    self.put_char(self.underscore_list)
                    print(self.underscore_list)
        else:
            self.chances+=1
            self.put_image(photos[self.chances])

            if self.chances==7:
                self.game_lost = True
                self.message.set("You suck!")
                self.put_char(list(self.word))

        if "_" not in self.underscore_list:
            self.message.set("Siu")

        self.e1.delete(0, tk.END)
