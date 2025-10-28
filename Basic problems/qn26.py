# program to print daimond shaped star pattern, number of raws are entered by the user
n=int(input("Enter your number of rows:"))
for i in range(0,n+1): # the first line of the output will be a collection of spaces, bcz the range given for i starts from 0. you can also give 1, so the first line of output will be a star
    print(" "*(n-i),end="")
    print("*"*(2*i-1)) # here the expression (2*!-1) represents all odd numbers, buy changing the expression only, we can print more different patterns
for i in range((n-1),0,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))