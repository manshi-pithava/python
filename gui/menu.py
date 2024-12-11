from tkinter import *
from tkinter import colorchooser
t=Tk()
t.geometry('1000x1000')
my_menu=Menu()
t.config(menu=my_menu)
file=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='File',menu=file)
file.add_cascade(label='Open')
def col():
    color=colorchooser.askcolor()
    t.config(bg=color[1])
file.add_cascade(label='Color',command=col)

# canvass
c=Canvas(t,bg='pink',height=200,width=200)
line=c.create_line(10,10,200,200)
c.pack()
t.mainloop()

