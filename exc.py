try:
    n1=int(input("enter value of n1="))
    n2=int(input("enter value of n2="))
    n3=n1/n2
except NameError:
    print("name error is generated")
except ZeroDivisionError:
    print("division error occured ")
except:
    print("exception is occured ")
else:
    print("division ans:",n3)
