from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
N = None
FLIP_TIMER = str()

# ----------------------- Loading and Saving Data ------------------------------- #
try:
    data = pandas.read_csv("data/pending_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


# ------------------------ Changing Flash Cards --------------------------------- #
def flash_card_change():
    global N, FLIP_TIMER
    if FLIP_TIMER:
        window.after_cancel(FLIP_TIMER)
    # correct_button.config(state=DISABLED)
    # wrong_button.config(state=DISABLED)
    N = random.randint(0, len(data) - 1)  # Selecting Flash Card Word
    word = data.loc[N]
    french = word["French"]
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(card_text, text=french)
    FLIP_TIMER = window.after(3000, flip)


def flip():
    global N
    word = data.loc[N]
    english = word["English"]
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_text, text=english)
    # correct_button.config(state=NORMAL)
    # wrong_button.config(state=NORMAL)


# ------------------------------ Button Functions ------------------------------- #
def correct_answer():
    global N
    data.drop(index=N, inplace=True)
    flash_card_change()


def wrong_answer():
    flash_card_change()


# ------------------------------ User Interface ----------------------------------#
window = Tk()
window.title("French Fresher Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

# Load Images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
tick = PhotoImage(file="images/right.png")
cross = PhotoImage(file="images/wrong.png")
# Canvas Elements
canvas = Canvas(width=800, height=512, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_background = canvas.create_image(400, 256, image=card_front)
card_text = canvas.create_text(400, 256, font=("Ariel", 32, "normal"))

# Buttons
correct_button = Button(image=tick, command=correct_answer)
wrong_button = Button(image=cross, command=wrong_answer)
correct_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)
flash_card_change()
window.mainloop()

data.to_csv("data/pending_words.csv")
