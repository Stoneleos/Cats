from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Список доступных тегов
ALLOWED_TAGS = [
    'sleep', 'jump', 'smile', 'fight', 'black', 'white', 'red', 'siamese', 'bengal'
]

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def open_new_window():
    tag = tag_combobox.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_with_tag)
    if img:
        new_window = Toplevel()
        new_window.title("Cat Image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()


def set_image():
    img = load_image(url)
    if img:
        new_window = Toplevel()
        new_window.title("Cat Image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()


window = tk.Tk()
window.title("Cats!")
window_width = 200
window_height = 200

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# menu_bar = Menu(window)
# window.config(menu=menu_bar)

# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Файл", menu=file_menu)
# file_menu.add_command(label="Загрузить фото", command=open_new_window)
# file_menu.add_separator()
# file_menu.add_command(label="Выход", command=window.destroy)

# Метка "Выбери тег"
tag_label = Label(window, text="Выбери тег")
tag_label.pack()

tag_combobox = ttk.Combobox(window, values=ALLOWED_TAGS)
tag_combobox.pack()


tag_cat = Button(window, text="Котик по тегу", command=open_new_window)
tag_cat.pack()

random_cat = Button(window, text="Случайный котя", command=set_image)
random_cat.pack(pady=15)
url = "https://cataas.com/cat"


window.mainloop()