# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

a=int(input("Enter your number: "))
n1=int(str(a)*1) #str converts any value to string
n2=int(str(a)*2 ) 
n3=int(str(a)*3)
# variables n1,n2,n3 are created by converting the input integer "a" to a string and then back to an integer
print(n1+n2+n3)
