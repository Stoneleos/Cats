from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((500, 500), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error happened: {e}")
        return None


def open_new_window():
    tag = tag_entry.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window=Toplevel()
        new_window.title("Вот вам котик")
        new_window.geometry("600x600")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def exit():
    window.destroy()


window = Tk()
window.title("Cataas")
window.geometry("600x600")

tag_entry = Entry(window)
tag_entry.pack()

load_button = Button(window, text="Загрузить по тегу", command=open_new_window)
load_button.pack()

# update_button = Button(window, text="Обновить", command=set_image)
# update_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Еще кота?", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

label = Label()
label.pack()
url = "https://cataas.com/cat"

set_image()

window.mainloop()
