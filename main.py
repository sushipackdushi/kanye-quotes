from tkinter import *
import requests
from PIL import ImageTk, Image


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = ImageTk.PhotoImage(Image.open("background.png"))  # PIL solution
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quote is HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = ImageTk.PhotoImage(Image.open("kanye.png"))  # PIL solution
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()