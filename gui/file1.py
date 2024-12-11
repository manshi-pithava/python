from tkinter import *;
from tkinter import filedialog;
t=Tk()
t.geometry('700x700')
l=Label(t,text='DEMO OF FILEDIALOG:')
l.place(x=70,y=80)
def hello():
    filepath=filedialog.askopenfilename(filetypes={('text file','*.txt')})
    print("FILE PATH:-"+filepath)
    file=open(filepath,'r')
    data=file.read()
    print("data of this file :"+data)
hello()
b=Button(t,text="demo",command=hello)
b.place(x=90,y=90)
t.mainloop()