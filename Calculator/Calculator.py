from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

screen = Tk()
screen.title("Calculator")
screen.geometry("640x480")


def Operation():
     pass

fstLabel = Label(text="Enter first number").place(x=20, y=20)

fstNum = Entry(screen, width=5, justify=CENTER)
fstNum.place(height=30,x=50, y=50)

sndLabel = Label(text="Enter second number").place(x=160, y=20)

sndNum = Entry(screen, width=5, justify=CENTER)
sndNum.place(height=30,x=200, y=50)

listBar = ttk.Combobox(screen, values = ["+", "-", "*", "/", "//", "%", "^"])
listBar.place(width=50, height=30, x=200, y=100)
listBar.current(0)

operand = listBar.get()

#10 2 8 16

decimalLabel = Label(text="Десятичная система").place(x=10,y=150)
decimalSS = Label(screen,text=result,bg="white",width=4,height=2)
decimalSS.place(x=150, y=140)

binLabel = Label(text="Двоичная система").place(x=10, y=200)
binSS = Label(screen,text=result,bg="white",width=4,height=2)
binSS.place(x=150, y=190)

eightLabel = Label(text="Воьмеричная система").place(x=10, y=250)
eightSS = Label(screen,text=result,bg="white",width=4,height=2)
eightSS.place(x=150, y=240)

sixteenLabel = Label(text="Шестнадцатиричная система").place(x=10, y=300)
sixteenSS = Label(screen,text=result,bg="white",width=4,height=2)
sixteenSS.place(x=190, y=290)
#print(listBar.get())






screen.mainloop()
