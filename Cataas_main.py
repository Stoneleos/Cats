from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from pygame.examples.sprite_texture import load_img

window = Tk()
window.title("Cataas")
window.geometry("600x480")

label = Label()
label.pack()
url = "https://cataas.com/cat"
img = load_img(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
