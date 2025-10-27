# program to find the product of digits of a number 
n=int(input("Enter your number: "))
product_of_digits=1 #if this set as 0, the entire output will be zero, 0*anything=0
while n>0:
    digits=n%10
    product_of_digits*=digits
    n=n//10
print("Product of digits= ", product_of_digits)