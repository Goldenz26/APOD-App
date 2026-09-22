import datefunc
import tkinter as tk
from tkinter import messagebox
import APOD
from PIL import Image, ImageTk
import pic_info
import os

try:
    os.mkdir("ImageCache")
    print("Directory 'ImageCache' created")

except FileExistsError:
    print("Directory 'ImageCache' already exists")


def last_image():
    datefunc.set_current_date(datefunc.date_minus_one(datefunc.get_current_date()))
    APOD.save_image_from_date(datefunc.get_current_date())
    image_last = Image.open(f"./ImageCache/image_{datefunc.apodify(datefunc.get_current_date())}.png")
    image_last = image_last.resize((300, 300))
    image_last = ImageTk.PhotoImage(image_last)
    global image_label
    image_label.image = image_last#this is done because python garbage collection will destroy image so we assign it to the label_image variable
    image_label.config(image=image_last)
    global description
    description.config(text=f"{pic_info.title}\n{datefunc.get_current_date()}",font=("Courier New", 15))

def next_image():
    if datefunc.date_plus_one(datefunc.get_current_date()) <= datefunc.get_date_today():
        datefunc.set_current_date(datefunc.date_plus_one(datefunc.get_current_date()))
        APOD.save_image_from_date(datefunc.get_current_date())
        image_next = Image.open(f"./ImageCache/image_{datefunc.apodify(datefunc.get_current_date())}.png")
        image_next = image_next.resize((300, 300))
        image_next = ImageTk.PhotoImage(image_next)
        global image_label
        image_label.image = image_next#this is done because python garbage collection will destroy image so we assign it to the label_image variable
        image_label.config(image=image_next)
        global description
        description.config(text=f"{pic_info.title}\n{datefunc.get_current_date()}", font=("Courier New", 15))
    else:
        tk.messagebox.showwarning("Invalid date", "Date is in the future")




datefunc.set_current_date(datefunc.get_date_today())
APOD.save_image_from_date(datefunc.get_current_date())


root = tk.Tk()
root.title("APOD")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="black")
#initializing the image we got from our APOD api
image = Image.open(f"./ImageCache/image_{datefunc.apodify(datefunc.get_current_date())}.png")
image = image.resize((300,300))
image = ImageTk.PhotoImage(image)
button_next = tk.Button(root,text="-->",command=next_image,fg="white",bg="black")
button_last = tk.Button(root,text="<--",command=last_image,fg="white",bg="black")
image_label = tk.Label(root,image=image,bg="black")
button_next.pack(side="right",fill="both")
button_last.pack(side="left",fill="both")
description = tk.Message(root,text=f"{pic_info.title}\n{datefunc.get_current_date()}",font=("Courier New", 15),fg="white",bg="black")
description.pack(side="bottom",fill="both")

image_label.pack(side="top")
root.mainloop()














