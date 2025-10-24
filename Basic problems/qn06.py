# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum
n1=int(input("enter your first number: "))
n2=int(input("enter your second number: "))
n3=int(input("enter your third number: "))
a=n1+n2+n3
if (n1==n2==n3):
    
    print("since the numbers are equal=> ",a*3)
else:
    print("since the numbers are not equal=> ",a)