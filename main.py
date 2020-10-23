from tkinter import *
from tkinter import ttk 

root = Tk()
root.title('counterlite')
root.geometry('200x220')

#Variables
counter = IntVar(0)
increment = 3

#Define increase click
def addclick():
    counter.set(counter.get() + increment)
def minusclick():
    counter.set(counter.get() - increment)

#Define Increment
def addIncrement():
    increment + 1
def minusIncrement():
    increment + 1

#Define Increment window
def opennewwindow():
    newwindow = Toplevel()
    newwindow.title("Change Increment")
    newwindow.geometry("260x100")

    #labels in attr newwindow
    itext = Label(newwindow, textvariable=increment).pack()

    iupbtn = Button(newwindow, text='Increase', command=addIncrement).pack()
    idownbtn = Button(newwindow, text='Decrease', command=minusIncrement).pack()
    

#Show the variable
countLabel = Label(root, textvariable=counter, font='Helvetica 20').pack(pady=20)

#Buttons + and -
addbtn = ttk.Button(text='+', command=addclick).pack()
addbtn = ttk.Button(text='-', command=minusclick).pack()

root.attributes('-fullscreen', False)

def fullon():
    root.attributes('-fullscreen', True)

def fulloff():
    root.attributes('-fullscreen', False)

obtn = ttk.Button(text='Fullscreen On', command=fullon).pack()
fbtn = ttk.Button(text='Fullscreen Off', command=fulloff).pack()

root.mainloop()