from tkinter import *

calci = Tk()
calci.title("Simple Calculator")
calci.geometry("270x150")
glb=0

def add:
    a=(int)txt1
    b=(int)txt2
    c=a+b
    glb=c

def subs:
    a=(int)txt1
    b=(int)txt2
    c=a-b
    glb=c

def multiply:
    a=(int)txt1
    b=(int)txt2
    c=a*b
    glb=c

def div:
    a=(int)txt1
    b=(int)txt2
    c=a/b
    glb=c

num1=label(calci,text="Enter number")
num1.grid(row=1,column=1)
num2=label(calci,text="Enter number")
num2.grid(row=2,column=1)
txt1=entry(calci).grid(row=1,column=2)
txt2=entry(calci).grid(row=2,column=2)


plus = Button(calci, text=' + ', bg='red',command=add,)
plus.grid(row=3, column=1)

minus = Button(calci, text=' - ', bg='red',command=subs)
minus.grid(row=3, column=2)

multiply = Button(calci, text=' * ', bg='red',command=mul)
multiply.grid(row=3, column=3)

divide = Button(calci, text=' / ', bg='red',command=div)
divide.grid(row=3, column=4)

result = Button(gui, text=' = ', bg='red',command=result)
equal.grid(row=4, column=[2:3])

calci.mainloop()
