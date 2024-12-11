import matplotlib.pyplot as p
import numpy as n
s=[56,78,89,90]
stream=["net","cpp","ora","wd"]
col=['r','g','b','cyan']
exp=[0.1,0,0,0]
p.pie(s,labels=stream,colors=col,shadow=True,explode=exp)
p.show()