from tkinter import *
from tkinter import ttk

root = Tk()

#Variables
counter = IntVar(0)

#Define
def addclick():
    counter.set(counter.get() + 1)
def minusclick():
    counter.set(counter.get() - 1)

#Show the variable
countLabel = Label(textvariable=counter).pack()

#Buttons + and -
addbtn = ttk.Button(text='+', command=addclick).pack()
addbtn = ttk.Button(text='-', command=minusclick).pack()

root.mainloop()