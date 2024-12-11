from tkinter import *
t=Tk()
t.geometry('400x400')
s=Scrollbar(t)
s.pack(side=RIGHT,fill=Y)
lb=Listbox(t,yscrollcommand=s.set)
for i in range(100):

    lb.insert(i,i)
lb.pack(side=LEFT,fill=BOTH)
s.config(command=lb.yview)
t.mainloop()