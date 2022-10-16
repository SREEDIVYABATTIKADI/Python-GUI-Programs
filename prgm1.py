from tkinter import * 
top=Tk()
top.title("calculator")
top.geometry("570x600+100+200")
top.resizable(False,False)
top.configure(bg="black")
equation =""
def show(value):
    global equation
    equation+=value
    l.config(text=equation)
def clear():
    global equation
    equation=""
    l.config(text=equation)
def calculate():
    global equation
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="syntax error"
            equation=""
    l.config(text=result)
            
l=Label(top,width=25,height=2,text="",font=("arial",30))
l.grid(row=0,columnspan=5)
Button(top,text="C",width=5,height=1,font=("arial",30,"bold"),bg="light blue",fg="white",command=lambda:clear()).grid(row=1,column=0)
Button(top,text="/",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("/")).grid(row=1,column=1)
Button(top,text="%",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("%")).grid(row=1,column=2)
Button(top,text="*",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("*")).grid(row=1,column=3)

Button(top,text="7",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("7")).grid(row=2,column=0)
Button(top,text="8",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("8")).grid(row=2,column=1)
Button(top,text="9",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("9")).grid(row=2,column=2)
Button(top,text="-",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("/")).grid(row=2,column=3)

Button(top,text="6",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("6")).grid(row=3,column=0)
Button(top,text="5",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("5")).grid(row=3,column=1)
Button(top,text="4",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("4")).grid(row=3,column=2)
Button(top,text="+",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("+")).grid(row=3,column=3)


Button(top,text="3",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("3")).grid(row=4,column=0)
Button(top,text="2",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("2")).grid(row=4,column=1)
Button(top,text="1",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("1")).grid(row=4,column=2)
Button(top,text=".",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show(".")).grid(row=4,column=3)

Button(top,text="0",width=5,height=1,font=("arial",30,"bold"),bg="black",fg="white",command=lambda:show("0")).grid(row=5,column=0)
Button(top,text="=",width=5,height=1,font=("arial",30,"bold"),bg="orange",fg="white",command=lambda:calculate()).grid(row=5,column=1)

top.mainloop()
