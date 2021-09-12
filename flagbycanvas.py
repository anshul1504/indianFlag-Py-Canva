from tkinter import Tk
from tkinter import Canvas
from time import time,sleep
t=Tk()
t.resizable(0,0)
t.geometry("500x600")
c=Canvas(width=500,height=600,bg="cyan")
c.pack()

c.create_rectangle(50,520,150,500,width=2,fill="yellow",outline="brown")
c.create_rectangle(30,540,170,520,width=2,fill="yellow",outline="brown")

def show0():
    c.create_line(97,50,97,500,width=8,fill="black")

t.after(1000,show0)    
def show1():
    c.create_rectangle(100,50,400,100,width=2,fill="orange",outline="black")
    c.create_rectangle(100,150,400,100,width=2,fill="white",outline="black")
    c.create_rectangle(100,200,400,150,width=2,fill="green",outline="black")
    
t.after(3000,show1)

def show2():
    s=0
    for i in range(0,24):
        c.create_arc(210,150,280,100,start=s,extent=10,fill="blue",activefill="pink")
        s+=20
t.after(4000,show2)        
def show3():
    c.create_text(250,320,text="\"INDIAN Flag\"",font=("",30),fill="red")
    c.create_line(120,350,380,350,width=3,fill="black")

t.after(5000,show3)


t.mainloop()