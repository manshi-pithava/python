from tkinter import *
t=Tk()
t.geometry('400x400')

sc=Scale(t,orient=HORIZONTAL,from_=1,to=500,length=200,width=40)
sc.place(x=23,y=90)

t.mainloop()