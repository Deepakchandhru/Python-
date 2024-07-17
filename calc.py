from tkinter import *

def getnum():
    a = int(enterOne.get())
    b = int(enterTwo.get()) 
    return (a,b)

def add():
    try:
        x,y = getnum()
        result["text"] = x+y
    except:
        result["text"] = "Enter two valid numbers"


def sub():
    try:
        x,y = getnum()
        result["text"] = x-y
    except:
        result["text"] = "Enter two valid numbers"


def div():
    try:
        x,y = getnum()
        result["text"] = x/y
    except:
        result["text"] = "Enter two valid numbers"


def mul():
    try:
        x,y = getnum()
        result["text"] = x*y
    except:
        result["text"] = "Enter two valid numbers"
    
root = Tk()
numOne = Label(root, text="Enter First Number:", font=("Calibri", 14))
enterOne = Entry(root)
numTwo = Label(root, text="Enter Second Number:", font=("Calibri", 14))
enterTwo = Entry(root)

add = Button(root, text="+", width=4, command=add)
sub = Button(root, text="-", width=4, command=sub)
div = Button(root, text="/", width=4, command=div)
mul = Button(root, text="X", width=4, command=mul)

result = Label(root,  font=("Calibri", 16))

numOne.grid(row=0, column=0, columnspan=6)
enterOne.grid(row=0, column=6)
numTwo.grid(row=1, column=0, columnspan=6)
enterTwo.grid(row=1, column=6)

add.grid(row=2, column=2)
sub.grid(row=2, column=3)
div.grid(row=2, column=4)
mul.grid(row=2, column=5)
result.grid(row=3, column=0, columnspan=8)

root.mainloop()