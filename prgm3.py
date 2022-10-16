from tkinter import *
top=Tk()
Label(top,text="enter number 1",bg="pink").grid(row=0,column=0)
Label(top,text="enter number 2",bg="pink").grid(row=1,column=0)
res=Label(top,text="result",bg="light blue")
res.grid(row=2,column=0)
num1=StringVar()
num2=StringVar()
num3=StringVar()
e1=Entry(top,textvariable=num1)
e1.grid(row=0,column=1)
e2=Entry(top,textvariable=num2)
e2.grid(row=1,column=1)
e3=Entry(top,textvariable=num3,fg="black")
e3.grid(row=2,column=1)
def calculate():
        try:
            n1=int(num1.get())
            n2=int(num2.get())
            result=n1/n2
            num3.set(result)
            e3.config(bg="light green")
        except ZeroDivisionError:
            e3.config(bg="red")
            e3.insert(0,"invalid")
        except:
            e3.config(bg="red")
            e3.insert(END,"Give proper entries")
Button(top,text="Divide",font=("arial",20,"bold"),height=2,width=5,bg="orange",command=calculate).grid(row=3,column=1)
