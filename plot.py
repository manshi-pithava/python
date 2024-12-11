import matplotlib.pyplot as p
import numpy as n
x=n.array([5,10,15])
y=n.array([0,5,10])

# y=n.array([10,20,5,70,89])
font1={
    "family":"calibri",
    "size":20,
    "color":"red"
}
p.xlabel("x-axes",fontdict=font1)
p.ylabel("y-axes",fontdict=font1)
p.title("....demo....")
# p.plot(x)
p.plot(y,marker='|',ls="dashed",linewidth=2)
# p.grid()
p.grid()
p.savefig('plot.png')
p.show()
