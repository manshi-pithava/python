def avg(marks):
    assert len(marks)!=0,"list empty"
    return sum(marks)/24
    
marks1=[543,518,518,492]
marks2=[519,509,537,492]
marks3=[521,497,522,508]
marks4=[469,513,534,505]

print("viral",avg(marks2))
print("pooja",avg(marks3))
print("amisha",avg(marks4))
print("mansi",avg(marks1))

print(avg(marks2),avg(marks1),avg(marks3),avg(marks4))