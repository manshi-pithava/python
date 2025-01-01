print(4 + 3 % 5)
# Explanation: The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i += 1
# note:) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction
x=1
print("bit-wise",x<<2)
# Explanation: The binary form of 1 is 0001.
#  The expression x<<2 implies we are performing bitwise
#  left shift on x. This shift yields the value: 0100, 
# which is the binary form of the number 4.
print(2**(3**2),(2**3)**2,2**3**2)
# Explanation: Expression 1 is evaluated as: 2**9, 
# which is equal to 512. 
# Expression 2 is evaluated as 8**2, which is equal to 64. 
# The last expression is evaluated as 2**(3**2). 
# This is because 
# the associativity of ** operator is from right to left. 
# Hence the result of the third expression is 512.


l=[1, 0, 2, 0, 'hello', '', []]
list(filter(bool, l))
print(l)