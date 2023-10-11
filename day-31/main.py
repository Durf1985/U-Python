from tkinter import *
import pandas
import random

# import time

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"
CARD_FRONT_COLOR = "#FFFFFF"
try:
    data = pandas.read_csv("data/words_to_learn.cvs.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
random_word = {}


def new_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data)
    card_canvas.itemconfig(language, text="French", fill="black")
    card_canvas.itemconfig(word, text=random_word["French"], fill="black")
    card_canvas.itemconfig(card_color, image=card_front)
    flip_timer = window.after(3000, func=right_answer)


def right_answer():
    card_canvas.itemconfig(card_color, image=card_back)
    card_canvas.itemconfig(language, text="English", fill="white")
    card_canvas.itemconfig(word, text=random_word["English"], fill="white")


def is_known():
    data.remove(random_word)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.cvs", index=False)
    new_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=right_answer)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_color = card_canvas.create_image(400, 275, image=card_front)
language = card_canvas.create_text(380, 150, text="", font=("Helvetica", 20, "italic"), justify="center")
word = card_canvas.create_text(390, 270, text="", font=("Helvetica", 30, "bold"), justify="center")
card_canvas.grid(column=0, row=0, columnspan=3)

know = PhotoImage(file="images/right.png")
know_button = Button(image=know, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
know_button.grid(column=2, row=4)

unknown = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
unknown_button.grid(column=0, row=4)
new_word()
window.mainloop()
