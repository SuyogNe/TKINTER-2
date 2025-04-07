from tkinter import *

root =Tk()
root.title("Image Viewer")
root.geometry("800x600")

def topwin():
    top=Toplevel()
    top.title("Top Window")
    top.geometry("400x300")
    l2=Label(top,text="This is a top window",font=("Arial",20))
    l2.pack()

    top.mainloop()

l=Label(root,text="This is root window")
button=Button(root,text="Open Top Window",command=topwin,font=("Arial",20),bg="blue",fg="white")

l.pack()
button.pack()

root.mainloop()