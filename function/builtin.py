import math
import random
import calendar
import datetime
print('---------------------------calender---------------------------------')
cal=calendar.month(2005,1)
print(cal)
print('---------------DATE -TIME----------------')
a=datetime.datetime.now()
print("DATE TIME:",a)
print(a.strftime('%B'))#current month
print(a.strftime('%d/%b/%y'))
print(a.strftime('%d %b,%y'))
print(a.strftime('%d %b,%y'))
print(a.strftime('%a'))
print(a.strftime('%A'))

print(a.strftime('%w'))
print(a.strftime('%d'))
print(a.strftime('%b'))
print(a.strftime('%B'))
print(a.strftime('%m'))
print(a.strftime('%M'))
# print(a.strftime('%p %M %s'))
 




print('--------------------------MATH FUNCTION--------------------')
print('min :',min(23,45,778,43,2.66))
print('max :',max(23,45,778,43,2.66))
print('abs :',abs(-23))
#WHEN THE O/P GIVE OUTSIDE OS THEN IMPORT A MODULE DEPEND ON USE OF FUNCTION
print('floor:',math.floor(-7.009))#give a floor(small)value
print('ceil :',math.ceil(-7.009))#give a ceil(top) value
print('sqrt :',math.sqrt(789))#square root of any given value
print('PI   :',math.pi)#value of pi


print('--------------------------RANDOM FUNCTION--------------------')
#1.random range():-give a random value between range you can give the argument,use like OTP,mobileno
#2.choice(): this function is use when less number of argument and return op like in random
print('randomrange(1,7878):-',random.randrange(1,7878))
ch=[1,2,3,4,5,6,7,8,9,0]
str="mansi_pithava@787878"
print('choice(number list)            :-',random.choice(ch))
print('choice( string)            :-',random.choice(str))

print('-----------------------STRING FUNCTION------------------')
#-----> STRING FUNCTION USE THEN NO NEED TO ADD/IMPORT ANY MODULE UNLIKE A MATH ,RANDOMetc....
print('LOWER():- CONVERT UPPER TO LOWER'.lower())
print('UPPER():- CONVERT  LOWER TO UPPER'.upper())
print('title():-the every word in sentance  first char. is capital '.title())
print('find():-','find the index of char OR string'.find('char'),'char index a=','char index:-'.find('a'),'find fun')
o="i like india"
n=o.replace("like","love")
print('replace( , ):- this fun is used in replace str or char. it take a 2 parameter 1.find a old string 2. change to new string',o,'=',n)
print('capitalize(): first char of string is capital'.capitalize())
print('-------BOOLEAN VALUE RETURN ARE 3 FUN------')
print('1.ISLOWER():','RETURN FALSE'.islower())
print('2.isupper():','return false'.isupper())
print('3.isalpha()true:','true'.isalpha())
ch=[" hii "," kijhj0 "," uyuery "]
j="~".join(ch)
print('join():-join a string ,collection, list etc..using a symbol-->',j)

print('---------------------LIST-----------------------------')
l=[4,6,5,4,"  ",32,"kjjlk l    "]
print(l)
print('list append(): add item in list ',l.append(90),l.append(90))
print(l)
print('--------------------------------------------------')

print("len(l): list of items",len(l))
print('--------------------------------------------------')

print("list.insert( ,): insert item in list with specified index and value")
print(l.insert(2,"mansi"),l)
print('--------------------------------------------------')

print("index():index of value in list `mansi`",l.index(90))
print('--------------------------------------------------')
print("count(): count the value of list one value is how many times in list.`90`",l.count(90))
print('--------------------------------------------------')
print("remove(value):remove the value from list`kjjlk l    `",l.remove("kjjlk l    "),l)
print('--------------------------------------------------')
l1=["Dhruviii","priyansh","pream","manv","kaushal","mansi"]
print('sort():list formate in sorting order with all list items are same types',l1.sort())
print(l1)
print('--------------------------------------------------')
print('l.reverse(): list can be arrange in reverse order',l1.reverse())
print(l1)

print('------------------------  TUPLE   --------------------------')
T=(78.090,9000.66,89.5,906,4440.90)
print('len:',len(T))
print('max:',max(T))
print('min',min(T))
print('sum',sum(T))

print("---------------------DICTIONARY  --------------------------")
# built in dictionary function
d1={
    13:169,
    "mansi":"bcaty",
    "manv":"6th",
    "kaushal":"b.voc it"
}
d2={
    "k2":"v2",
    "vira'":"bcaty",
    "devanshi":"6th",
    "ridham":"lkg"
}
d4={
    "k2":"v2",
    "vira'":"bcaty",
    "devanshi":"6th",
    "ridham":"lkg"
}
d3={
    "k2":"v2",
    "vira'":"bcaty",
    "devanshi":"6th",
    "ridham":"lkg"
}

print('cmp(d1,d2):compare dict element of both dictionary',)
print('len(d1):total length of d1=',len(d1))
# print("str(d1):produce a printable string representation of dict \nd1=",str(d1))
print("type(var):return the type of variable d1=",type(d1))
print("---------------------METHODS OF DICTIONARY  --------------------------")
print("d3.clear()",d3.clear())
print(d3)
print('d2.copy()',d2.copy)
a="f1","f2","f4"
b="avd","FEf","KIK"
ans=d1.fromkeys(a,b)


print('d1.fromkeys()',ans)
print(d1.values())
print(d1.keys())
print(d2.update(d4))
print(d2.items())
print(d2.__hash__)
