from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_toLearn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # print(current_card["French"])
    canvas.itemconfig(card_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=back_img)


def is_known():
    to_learn.remove(current_card)
    data_d = pandas.DataFrame(to_learn)
    data_d.to_csv("data/words_toLearn.csv", index=False)
    next_card()


window = Tk()
window.title("Word-Flash")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

card_img = canvas.create_image(400, 263,  image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross, highlightthickness=0, command=next_card)
unknown_btn.grid(column=0, row=1)

tik = PhotoImage(file="images/right.png")
known_btn = Button(image=tik, highlightthickness=0, command=is_known)
known_btn.grid(column=1, row=1)

next_card()

window.mainloop()