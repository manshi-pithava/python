# import tkinter
from tkinter import *
t=Tk()
t.geometry('500x500')
f=('Times New Roman',30,'bold')
# t.resizable(False,False)
l1=Label(t,text="shree ganeshay namh!",font=f,bg='#679f90')
# l1.pack(side=LEFT)
l1.place(x=50,y=70)
t.mainloop()