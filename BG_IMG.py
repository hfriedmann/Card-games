from tkinter import *
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk() 
# open image
image1 = Image.open('bg.jpg')
image2 = Image.open('p1.png')

image1.paste(image2, (251, 196), image2)

tkimage = ImageTk.PhotoImage(image1)

panel1 = Label(root, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)
root.mainloop()
