#program to sum two given integers. However, if the sum is between 15 and 20 it will return 20,the numbers are entered by the user.

def function(a,b):
    sum=a+b
    if sum>15 and sum<20:
        return 20
    else:
        return sum
n1=int(input("Enter your first number"))
n2=int(input("Enter your second number"))
a=function(n1,n2)
print(a)
