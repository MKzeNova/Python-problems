# program to sort three integers without using conditional statements and loops.
n1=int(input("Input first number: "))
n2=int(input("Input second number: "))
n3=int(input("Input third number: "))
x=min(n1,n2,n3) # find the min value among n1,n2,n3
y=max(n1,n2,n3) # find the max value among n1,n2,n3
z=(n1+n2+n3)-(x+y) # calculating the third value, ie the middle number, bcz we already know first number min value, and last number max value
print("Numbers in sorted order: ",x,z,y)