import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageOps, ImageTk


# global variables
original_image = None
image_preview = None

# effects
def show_image(img):
    global image_preview
    img = img.resize((300, 300))
    image_preview = ImageTk.PhotoImage(img)
    image_label.config(image=image_preview)

def open_image():
    global original_image
    filepath = filedialog.askopenfilename(filetypes=[("images", "*.jpg *.jpeg *.png")])
    if not filepath:
        return
    original_image = Image.open(filepath)
    show_image(original_image)


def save_image(img, name):
    img.save(name)
    messagebox.showinfo("Saved", f"Picture saved as {name}")

