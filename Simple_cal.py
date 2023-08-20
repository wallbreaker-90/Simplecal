from tkinter import *
import tkinter as tk
window = tk.Tk()
window.resizable(False,False)
window.title("Calculator")
window.geometry("400x420")

def clear():
    result=""
    resultL.config(text=result)

def add():
    try:
        num1 = int(Num1.get())
        num2 = int(Num2.get())
        result = num1 +  num2
        resultL.config(text=result)
    except ValueError:
        resultL.config(text="Invalid input")


def sub():
    try:
        num1 = int(Num1.get())
        num2 = int(Num2.get())
        result = num1 - num2
        resultL.config(text=result)
    except ValueError:
        resultL.config(text="Invalid input")


def miv():
    try:
        num1 = int(Num1.get())
        num2 = int(Num2.get())
        result = num1 * num2
        resultL.config(text=result)
    except ValueError:
        resultL.config(text="Invalid input")


def div():
    try:
        num1 = int(Num1.get())
        num2 = int(Num2.get())
        result = num1 / num2
        resultL.config(text=result)
    except ValueError:
        resultL.config(text="Invalid input")


title_label = tk.Label(width=20, text="Simple Calculator", font=("Arial", 30))
title_label.pack()
resultL = Label(window, width=20, height=3, font=('Arial', 20))
resultL.place(x=1,y=230)

num=tk.Label(window,text="Enter Number 1",font=('Arial',20))
num.place(x=15, y=68)
Num1 = tk.Entry(window, font=("Arial", 20))
Num1.place(x=15, y=100)
num2=tk.Label(window,text="Enter Number 2",font=('Arial',20))
num2.place(x=15, y=140)
Num2 = tk.Entry(window, font=("Arial", 20))
Num2.place(x=15, y=180)
resL=tk.Label(window,text="Result:",font=('Arial',20))
resL.place(x=15, y=220)

B_mod = Button(window, text="/", width=3, height=1, font=('Arial', 20), command=div)
B_mod.place(x=15, y=320)
B_Miv = Button(window, text="x", width=3, height=1, font=('Arial', 20), command=miv)
B_Miv.place(x=80, y=320)
B_Sub = Button(window, text="-", width=3, height=1, font=('Arial', 20), command=sub)
B_Sub.place(x=145, y=320)
B_add = Button(window, text="+", width=3, height=1, font=('Arial', 20), command=add)
B_add.place(x=210, y=320)
B_clear=Button(window, text="C", width=3, height=1, font=('Arial', 20), command=clear)
B_clear.place(x=290, y=320)
window.mainloop()
