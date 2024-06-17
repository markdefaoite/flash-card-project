BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.create_image(400, 265, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

language_label = Label(text="Language goes here", font=("Ariel", 40, "italic"), justify="left")
language_label.place(x=400, y=150)

word_label = Label(text="Word goes here", font=("Ariel", 60, "bold"), justify="center")
word_label.place(x=400, y=263)

window.mainloop()