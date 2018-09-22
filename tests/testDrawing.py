"""
    You may need to install tkinter if there is an error on the from tkinter line
    File -> Settings -> Project Interpreter
    Green + over on the right

    Search tkinter and click install package
    If there's an error get dad/administrator to upgrade pip
        python -m pip install --upgrade pip
"""

# TODO Mia homework: read chapter 12 and start experimenting!
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()

mainloop()
