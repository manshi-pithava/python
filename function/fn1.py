#function argument demo
def demo(a):
    print("value of a=",a)#require argument
demo(9009)

def demo1(nm,ct):
    print("name:",nm,"\ncity:",ct)
demo1(nm="mansi",ct="than")#keyword argument

def demo2(a=90,b=900):#default argument
    print("a+b",a+b)


demo2(909)
demo2()
demo2(89,1)

def printinfo(a1,*t):
    print(a1,t)
    for i in t:
        print(i)
printinfo(89,9)

