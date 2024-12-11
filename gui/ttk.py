from tkinter import *
from tkinter import ttk
t=Tk()
t.geometry('200x200')
def select():
    # print('demo')
    import time

    while (pg['value']!=100):
        pg['value']+=20
        t.update_idletasks()
        time.sleep(2)
def stop():
    t.destroy()
    print('progress completed')

pg=ttk.Progressbar(length=200,mode='determinate')
pg.place(x=20,y=30)
b1=Button(t,text='START!',command=select)
b1.place(x=60,y=60)
b2=Button(t,text='STOP!',command=stop)
b2.place(x=110,y=60)
t.mainloop()