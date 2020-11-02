"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()

f1 = Frame()
l1 = Label(f1, text="Enter a Adjective:")
e1 = Entry(f1, text="Adjective")

f2 = Frame()
l2 = Label(f2, text="Enter a Name")
e2 = Entry(f2, text="Name")

f3 = Frame()
l3 = Label(f3, text="Enter a Noun")
e3 = Entry(f3, text="Noun")

f4 = Frame()
f5 = Frame()


def madLibs():
    pass


o1 = StringVar()
o2 = StringVar()
o3 = StringVar()
o4 = StringVar()
o5 = StringVar()
o1.set("Adjective")
o2.set("Person's Name")
o3.set("Noun")
o4.set("Plural Noun")
o5.set("Adjective")


win.mainloop()
