factorial=1
no=int(input('enter the no='))
if no<0:
    print('f not')
elif no==0:
    print("f=1")
else:
    for i in range(1,no+1):
        factorial=factorial*i
    print("ans:",factorial) 
