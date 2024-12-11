from tkinter import *
from tkinter import messagebox
import time
t=Tk()
t.geometry('500x500')
# t.resizable(False,False)

t.title('Login')
f=('Arial',9,'bold')

tl=time.strftime('%H:%M:%S')
# tim=Label(t,text=tl)
# tim.place(x=500,y=4)


def click():
    if len(var1.get())==0:
        # print('enter name')
        messagebox.showwarning('Warning..!','enter your name')
    else:
        # print('Name:- '+var1.get())
        # print('Password:- '+var2.get())
        # print('Gender:- '+str(v1.get()))
        messagebox.showinfo('Login','Login successfully at:'+str(tl)+'\n Your Password is: '+var2.get())
        


# label
l=Label(t,text='LOGIN',font=f )
l.place(x=90,y=5)
l1=Label(t,text='Name',font=f )
l1.place(x=35,y=40)

# Entry .. text box
# var 1 for get value 

var1=StringVar()
e1=Entry(t,text='Name',textvariable=var1)
e1.place(x=75,y=40)


l2=Label(t,text='Password',font=f)
l2.place(x=10,y=80)
var2=StringVar()
e2=Entry(t,textvariable=var2)
e2.place(x=75,y=80)


l3=Label(t,text="Gender",font=f)
l3.place(x=20,y=120)
# radio button

v1=IntVar()
r1=Radiobutton(t,text='Male',font=f,variable=v1,value=1)
r1.place(x=70,y=120)


v2=IntVar()
r2=Radiobutton(t,text='Female',font=f,variable=v1,value=2)
r2.place(x=130,y=120)


b1=Button(t,text='Login',font=f,command=click)
b1.place(x=105,y=160)

t.mainloop()