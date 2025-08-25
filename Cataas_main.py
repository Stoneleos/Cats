from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error happened: {e}")
        return None

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
