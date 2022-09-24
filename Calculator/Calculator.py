from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import math

def decimal_to_ss(x, ss):
    string = ""
    ost = 0
    letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    while(x >= ss):
        ost = x % ss
        x //= ss
        if(ost in letters):
            string += letters[ost]
        else:
            string += str(ost)

    string += str(x)
    return string[::-1]

screen = Tk()
screen.title("Calculator")
screen.geometry("400x340")

fstLabel = Label(text="Enter first number").place(x=20, y=20)

fstNum = Entry(screen, text="0", width=5, justify=CENTER)
fstNum.place(height=30,x=50, y=50)

sndLabel = Label(text="Enter second number").place(x=160, y=20)

sndNum = Entry(screen,text="1", width=5, justify=CENTER)
sndNum.place(height=30,x=200, y=50)

listBar = ttk.Combobox(screen, values = ["+", "-", "*", "/", "//", "%", "^"])
listBar.place(width=50, height=30, x=200, y=100)
listBar.current(0)

decimalLabel = Label(text="Десятичная система").place(x=10,y=150)
decimalSS = Label(screen, bg="white",width=10,height=2)
decimalSS.place(x=150, y=140)

binLabel = Label(text="Двоичная система").place(x=10, y=200)
binSS = Label(screen,bg="white",width=10,height=2)
binSS.place(x=150, y=190)

eightLabel = Label(text="Воьмеричная система").place(x=10, y=250)
eightSS = Label(screen,bg="white",width=10,height=2)
eightSS.place(x=150, y=240)

sixteenLabel = Label(text="Шестнадцатиричная система").place(x=10, y=300)
sixteenSS = Label(screen,bg="white",width=10,height=2)
sixteenSS.place(x=190, y=290)

def Operation(operand, fstNum, sndNum):
    try:
        if operand == "+": return fstNum + sndNum
        if operand == "-": return fstNum - sndNum
        if operand == "*": return fstNum * sndNum
        if operand == "/": return fstNum / sndNum
        if operand == "//": return fstNum // sndNum
        if operand == "%": return fstNum % sndNum
        if operand == "^": return int(math.pow(fstNum, sndNum))
    except Exception:
        print("Error with operand")
    return

def getNums():

    operand = listBar.get()
    fst = eval(fstNum.get())
    snd = eval(sndNum.get())
    result = Operation(operand,fst,snd)

    decimalSS.config(text=result)
    binSS.config(text=decimal_to_ss(result,2))
    eightSS.config(text=decimal_to_ss(result,8))
    sixteenSS.config(text=decimal_to_ss(result,16))

operationButton = Button(width=2,height=1,text="=", command=getNums).place(x=300,y=50)

screen.mainloop()
