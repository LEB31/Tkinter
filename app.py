# Tkinter Input/Output 4/18/2022
# Create a window
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


win = Tk()

def level1():
   first=Toplevel()
   first.configure(bg="#81BCA9")
   first.geometry('600x500')
   first.title('Start')
   # List 
   name = []
   p = []
   # Variables 
   user = un.get()
   name.append(user)
   up = pw.get()
   p.append(up)
   # Welcome User
   lb2 = Label(first, text = 'Hello ' + name[0] + '!')
   lb2.place(x=265, y= 150)

   # Exit the Program
   btn2 = Button(first, text = 'START', command=level2)
   btn2.place(width= 100, height= 50, x=250, y=250)

def level2():
   start=Toplevel()
   start.configure(bg="#EDEFA2")
   start.geometry('600x500')
   start.title("Let's Go!")


win.geometry('600x500')
win.title('Welcome!')
win.configure(bg="#BC8194")
# Label (Log in)
lb = Label(win, text='Log In')
lb.place(x=280, y=200)
# Label (Username)
lbun = Label(win, text='Username:')
lbun.place(x=205,y=250)
# Enter Username
un = Entry(win)
un.place(x=270,y=250)
# Label (Password)
lbun1 = Label(win, text='Password:')
lbun1.place(x=205,y=275)
# Enter Username
pw = Entry(win, show='*')
pw.place(x=270,y=275)
# Open Second Window
btn = Button(win, text ='Submit', command=level1)
btn.place(x=275, y=315)

win.mainloop()

