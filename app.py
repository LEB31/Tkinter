# Tkinter Input/Output 4/18/2022
import tkinter as Tk
from tkinter import *

win = Tk()
# Create a window
win.title = "Title"
win.geometry('600x500')
# Change background 
win.configure(bg= 'light blue')

# Exit Button
exit = Button(win, text="Exit", command=win.quit)
exit.place(height=20, x=300, y=300)

win.mainloop()