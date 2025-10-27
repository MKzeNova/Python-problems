# program to check if the sum of digits of a number is an even or odd number.
n=int(input("Enter your number: "))
sum_of_digits=0
while n>0:
    digits=n%10
    sum_of_digits+=digits
    n=n//10
if sum_of_digits%2==0:
    print("Sum of digits is even : ",sum_of_digits)
else:
    print("Sum of digits is odd : ",sum_of_digits)