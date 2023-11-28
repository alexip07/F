import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
to_learn = {}
current_card = {}
# Using pandas we create a data frame for the csv file, so we can use later on the game
try:
    df = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


# Function to change the words
def next_card():
    """it uses the dataframe created with pandas to get a random French word and display it on the card"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


# Flip the card function
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)


# The function that removes the word if the user knows them
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()


# Window setup
window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# Canvas setup
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="png/card_front.png")
card_back = tk.PhotoImage(file="png/card_back.png")

card_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons setup
correct = tk.PhotoImage(file="png/right.png")
correct_button = tk.Button(image=correct, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

wrong = tk.PhotoImage(file="png/wrong.png")
wrong_button = tk.Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
