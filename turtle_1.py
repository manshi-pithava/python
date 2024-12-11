# import turtle
from turtle import *
t=Turtle()
t.pensize(5)
t.penup()
t.goto(-150,50)


for i in range(4):
    t.pendown()
    t.forward(100)
    t.left(90)
t.hideturtle()

t.pensize(5)
t.penup()
t.goto(10,50)
t.pendown()
t.begin_fill()
t.color('pink')
for i in ['red','green','blue','magenta']:
    t.color(i)
    t.pendown()
    t.forward(100)
    t.left(90)
    
t.color('pink')
t.end_fill()   
hideturtle()
# t.end_fill()

mainloop()