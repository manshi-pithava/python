from tkinter import *
from tkinter import filedialog
t=Tk()
t.geometry('600x600')
header=('Arial',15,'bold')
f=('Arial',10,'bold')

f1=Frame(t,background='#909fff',height=400,width=400,border=5)
f1.pack(side=TOP)
l1=Label(f1,text='LOGIN',font=header,bg='#909fff')
l1.place(x=160,y=20)

l2=Label(f1,text='Name',font=f,bg='#909fff')
l2.place(x=90,y=60)
v1=StringVar()
e1=Entry(f1,text='name',textvariable=v1)
e1.place(x=130,y=60)

def get():
    print('your name:',v1.get())
def opens():
    print('open demo')
    filepath=filedialog.askopenfilename(filetypes={('text file','*.txt')})
    t.title(filepath)
    file=open(filepath,'w')
    file.write(e1.get())
   
def save():
    print('save demo')
    

b1=Button(f1,text='insert',command=get)
b1.place(x=140,y=100)
b2=Button(f1,text='open',command=opens)
b2.place(x=200,y=100)
b3=Button(f1,text='save',command=save)
b3.place(x=250,y=100)
t.mainloop()