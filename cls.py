# class emp:
#     def display(self):
#         print("emp method")
# e=emp()
# e.display()
class student:
    name="mansi"
    ct="thangadh"
    def __init__(self) -> None:
        print("default")
    def __init__(self,name):
        self.name=name
s1=student("smith")
print(s1.name)
print(s1.ct)
print(s1.name,s1.ct)
print(student.ct)
print(student.name)