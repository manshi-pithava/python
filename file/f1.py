file=open("demo.txt",'rt')
print("Mode of file:",file.mode)
print("Name of file:",file.name)
print("file close:",file.closed)
# file.close()
# print("file close:",file.closed)
file.write("Python is programming lang")
str=file.read(10)
print(str)
