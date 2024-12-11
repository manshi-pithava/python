print("mansi panchal")
a=23
b=42
a=" "
b="..."

print(" value of a=",a,"value of b=",b)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

a=int(input("enter the value of a= "))
b=int(input("enter the value of b= "))

print('---------------------Arithmatic operator-----------------------')


print("add ",a+b)
print("sub ",a-b)
print("mul ",a*b)
print("div ",a/b)
print("mod ",a%b)
print("floor divider ",a//b)
print("--------------------logical operator----------------")
print(a,">10and20< ",b,a>10 and b>20)
print(a,"< ",b,a>10 or b>20)
print(a,"< ",b,)

print("~~~~~~~~~~~~~~~~~~~relational operator~~~~~~~~~~~~~~~~~~~ ")

print(a,"< ",b,a<b)
print(a,"> ",b,a>b)
print(a,"<= ",b,a<=b)
print(a,">= ",b,a>=b)
print(a,"== ",b,a==b)
print("~~~~~~~~~~~~~~~~~~~Assignment operatopr~~~~~~~~~~~~~~~~~~~ ")
a+=100
a-=5
a*=10
a/=10
a%=10
a//=10
print("add ",a)
print("sub ",a)

print("mul ",a)
print("div ",a)
print("mod ",a)
print("floor divider ",a//b)

print("~~~~~~~~~~~~~~~~~~~member ship~~~~~~~~~~~~~~~~~~~ ")

list=["78","oop",78,9.099,'9']
print(list)
print(list[2:])
print(list[2:6])
print('9 in list=',9 in list)
print('str 9 in list=','9' in list)

print('str 9 not in list=','9' not in list)
print('________________________1.Dictionory, 2.Tuple,3.List_______________________')

d={
    "k1":"v1",
    "k2":["klklklkl",90,90.999],
    "k3":9000
}
print(d)
print(d['k1'])
print('dictionary:=',"keys=",d.keys(),"values=",d.values())
t=('tuple',"ryreyge",90,90.0009,4.4444)
print("Tuple:-",t[4])

print("-----------------------condition ---------------")
a=int(input("enter the value of a="))
if a>0 :
    if a%2==0 :
        print("no is pos and even")
    else :
        print("no is pos and odd")  
else :
    if a%2==0 :
        print("no is nagative or even")
    else :    
          print("no is nagative or odd")

print("-------------------Loop------------------")

for i in range(1,11):
    print('-------------------------table=',i,'-------------------')
    for j in range(1,11):
        k=i*j
        print(i ,'*',j,'=',k)
    
for i in reversed(range(1,11)):
    if i==3:
        #pass
        #break
        continue
        print('if block')
    print(i) 






