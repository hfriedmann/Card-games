import random
import tkinter as tk
#i used this "as tk", because many scripts I was using did the same.
from tkinter.ttk import *
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Tarot")
window.geometry("700x700")
window.configure(background='black')

def update_the_picture():
    num=random.randint(0, 20)
    w.configure(image=images[num])
    #choose numbers between 0 and 20. I'm not sure why, but that's the only way the cards 0 and 21 were chosen

images=[]
for fname in range(0, 21):
    #open generic imgs, named as 0.jpg - 21.png
    img = ImageTk.PhotoImage(Image.open("%d.jpg" % (fname)).resize((200,332), Image.ANTIALIAS))
    #to sized photos i used ths: resize
    images.append(img)
    
w = tk.Label(window, image = img, bg="black")
w.pack(side = "bottom", fill = "both", expand = "yes")
b = tk.Button(window, text="new card", command = update_the_picture).pack()
#click button, pick new card.

update_the_picture()

window.mainloop()
