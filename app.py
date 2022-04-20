# Tkinter Input/Output 4/18/2022
# Create a window
from tkinter import *
from turtle import bgcolor

win = Tk()

def level1():
   first=Toplevel()
   first.geometry('600x500')
   first.title('Start')
   first.configure(bg='light pink')
   btn2 = Button(first, text = 'Exit', command=quit)
   btn2.place(width= 100, height= 50, x=250, y=250)


win.geometry('600x500')
win.title('Welcome!')
win.configure(bg='light blue')

btn = Button(win, text ='Start', command=level1)
btn.place(width= 100, height= 50, x=250, y=250)

win.mainloop()

