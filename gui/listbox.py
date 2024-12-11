from tkinter import *
t=Tk()
t.geometry('500x500')
t.title("demo of listbox")
pos=0
def select():
     a=l.index(ANCHOR)
     print('------------------------------------')
     print('index of selected item',a)
     b=l.delete(ANCHOR)
     print('delete',b)
     print('------------------------------------')
    #  i=l.insert(ANCHOR)
    #  print(i)
    #  print('------------------------------------')

     
l=Listbox(t)


l.insert(1,"BCA")
l.insert(2,"MCA")
l.insert(3,"BBA")
l.insert(4,"MBA")
l.insert(5,"BBOM")
l.insert(6,"BCOM")
l.place(x=50,y=50)

b=Button(t,text='delete',command=select)
b.place(x=200,y=200)

t.mainloop()