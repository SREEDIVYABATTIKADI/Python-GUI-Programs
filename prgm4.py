from tkinter import *
top=Tk()
var=StringVar()
var.set("white")
def setlight():
    top.config(bg=var.get())
Radiobutton(top,text="red light",variable=var,value="red",command=setlight).pack(anchor=W)
Radiobutton(top,text="yellow light",variable=var,value="yellow",command=setlight).pack(anchor=W)
Radiobutton(top,text="green light",variable=var,value="green",command=setlight).pack(anchor=W)
top.mainloop()
