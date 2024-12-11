from tkinter import *
from tkinter import ttk

t=Tk()
t.geometry('800x800')
f=('Arial',10,'bold')
lan=['j2ee','python','cs','project','p1','p2']
cb=ttk.Combobox(values=lan,font=f)

cb.place(x=80,y=80)
t.mainloop()
