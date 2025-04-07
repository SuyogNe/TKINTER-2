from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("800x600")

def msg():
    messagebox.showwarning("ALERT", "SYSTEM VIRUS DETECTED")

button=Button(root,text="Scan for virus",command=msg,font=("Arial",20),bg="red",fg="white")
button.place(x=50,y=50)

root.mainloop()
