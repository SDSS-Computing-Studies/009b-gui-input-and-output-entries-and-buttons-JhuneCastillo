"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()

eoutput = StringVar()
eoutput.set("Answer")


def trinomial():
    a = 1
    b = int(e1.get())
    c = int(e2.get())

    a1 = (-b + (b**2-4*a*c) ** (1/2)) / (2)
    a2 = (-b - (b**2-4*a*c) ** (1/2)) / (2)

    o1 = str(-1*a1)
    o2 = str(-1*a2)
    o3 = ("(x + " + o1 + ")" + "(x + " + o2 + ")")

    p1.delete(0, END)
    p1.insert(0, o3)


l1 = Label(win, text="Input Value For B And C (A Will Always Be 1)")
l2 = Label(win, text="ax^2 - ")
l3 = Label(win, text="x + ")
b1 = Button(win, text="=", command=trinomial)
e1 = Entry(win, text="B")
e2 = Entry(win, text="C")
p1 = Entry(win, text="Answer", textvariable=eoutput)

l1.pack()
l2.pack(side=LEFT)
e1.pack(side=LEFT)
l3.pack(side=LEFT)
e2.pack(side=LEFT)
b1.pack(side=LEFT)
p1.pack()

win.mainloop()
