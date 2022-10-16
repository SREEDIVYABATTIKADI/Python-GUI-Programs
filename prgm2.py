from tkinter import *
top=Tk()
Label(top,text="Enter a number",bg="pink",fg="black").grid(row=0)
t=Text(top,bg="orange",fg="white",height=2,width=5)
t.grid(row=0,column=1)
Label(top,text="result",bg="pink",fg="black").grid(row=1)
t1=Text(top,bg="orange",fg="white",height=2,width=5)
t1.grid(row=1,column=1)

def factorial():
    n=int(t.get("1.0","end-1c"))
    if n==0 or n==1:
        t1.delete("1.0","end-1c")
        t1.insert(END,1)
    else:
        result=1
        for i in range(1,n+1):
            result=result*i
        t1.delete("1.0","end-1c")
        t1.insert(END,result)
b=Button(top,text="compute",command=factorial,bg="light blue")
b.grid(row=2,column=1)
