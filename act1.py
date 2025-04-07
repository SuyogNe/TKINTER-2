from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Image Viewer")
root.geometry("800x600")

upload=Image.open("image.png")
Image=ImageTk.PhotoImage(upload)

label=Label(root,image=Image)
label.place(x=50, y=50)
label1=Label(root,text="This is an image",font=("Arial",20))
label1.place(x=50, y=300)

root.mainloop()