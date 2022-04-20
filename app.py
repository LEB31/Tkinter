# Tkinter Input/Output 4/18/2022
# Create a window
from tkinter import *


win = Tk()

def level1():
   first=Toplevel()
   first.geometry('600x500')
   first.title('Start')
   first.configure(bg='light pink')
   # Exit the Program
   btn2 = Button(first, text = 'Exit', command=quit)
   btn2.place(width= 100, height= 50, x=250, y=250)


win.geometry('600x500')
win.title('Welcome!')
win.configure(bg='light blue')
# Label (Log in)
lb = Label(win, text='Log In')
lb.place(x=280, y=200)
# Label (Username)
lbun = Label(win, text='Username:')
lbun.place(x=210,y=250)
# Enter Username
un = Entry(win)
un.place(x=270,y=250)
# Variables
user = un.get()
# Open Second Window
btn = Button(win, text ='Submit', command=level1)
btn.place(x=275, y=300)

win.mainloop()

