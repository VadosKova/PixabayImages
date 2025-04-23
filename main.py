import requests
from tkinter import *
from PIL import Image, ImageTk
import random

API_KEY = "49887797-4504305467ee5706dfdb7b3be"

def update_image():
    url = f"https://pixabay.com/api/?key={API_KEY}&image_type=photo"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["hits"]:
            img_url = random.choice(data["hits"])["largeImageURL"]
            img_data = requests.get(img_url).content
            ext = img_url.split('.')[-1]


root = Tk()
root.title("Pixabay Images")
root.geometry("500x500")

label = Label(root)
label.pack(padx=20, pady=20)

Button(root, text="Next").pack(pady=10)


root.mainloop()