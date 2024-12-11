from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
t=Tk()
t.geometry('200x200')
f=('Arial',15)
def hello():
    res=simpledialog.askstring("insert","what is your stream")
    if res is not None:
        print(res)
        messagebox.showinfo("info","your stream is:"+res)
    else:

        print("enter your stream")
b=Button(t,text="CLICK",command=hello)
b.pack()
t.mainloop()