#Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.
def calculation(a,b):
    addition=a+b
    substraction=a-b
    return addition, substraction
result=calculation(23,3)
print("result=", result)