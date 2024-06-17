from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Language goes here", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word goes here", font=("Ariel", 60, "bold"))


right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0)
known_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0)
unknown_button.grid(row=1, column=0)


window.mainloop()
