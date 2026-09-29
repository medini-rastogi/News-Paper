## -----  Desinged a News paper with tkinter  ----- ##

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)
root.title("My_Newspaper")

## HEADING
dahi = Label(text = "New Mornings - New Adventures", font = ("Times New Roman", 24, "bold"), fg = "brown4", 
        bg = "RosyBrown1", relief = "groove", borderwidth = 5)

## IMAGE 1
raw_image = Image.open("/home/medini_rastogi/Documents/vs code/News_Paper/image4.jpeg")
second_image = raw_image.resize((500, 250))
#Converting the image for tkinter
gulabi = ImageTk.PhotoImage(second_image)
gulab = Label(image = gulabi, bg = "antique white")

## IMAGE 2
raw__image = Image.open("/home/medini_rastogi/Documents/vs code/News_Paper/image3.jpeg")
second__image = raw__image.resize((500, 250))
raaz = ImageTk.PhotoImage(second__image)
raazi = Label(image = raaz, bg = "antique white")

## ARTICLE 1
with open("/home/medini_rastogi/Documents/vs code/News_Paper/Nature_article.md", "r") as file:
    scenery_text = file.read()
kajal = Label(text = scenery_text, wraplength = 450, padx = 15, fg = "PaleGreen4", bg = "antique white",
        font = ("Georgia", 12, "italic"))

## SHORT ARTICLE 1
kamal = Label(text = "To make a prairie it takes a clover and one bee,\nOne clover, and a bee,\nAnd " \
"revery.\n\t\t- Emily Dickinson", font = ("Times New Roman", 11, "italic"), fg = "OliveDrab4", bg = "antique white", 
justify = "left")

dahi.pack(side = "top", fill = "x")
kajal.pack(side = "left", anchor = "nw", fill = "y")
gulab.pack(anchor = "ne", side = "top", fill = "x")
kamal.pack(side = "top", fill = "x")
raazi.pack(side = "bottom", fill = "x")

root.mainloop()