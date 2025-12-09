# write a program to check if a given number is armstrong or not.
# Armstrong number is a number that is equal to the sum of its own digits, each raised to a power equal to the number of digits in the number
# eg: 153=1^3+ 5^3+ 3^3
number=int(input("Enter your number:"))
temp=number       # we want to use the "number" in many places, so we must save a copy of the                        number to another variable 
no_of_digits=0
while number>0:
    digit=number%10
    no_of_digits=no_of_digits+1
    number=number//10           #number of digits are calculated here    
print("number of digits of","\"",temp,"\":",no_of_digits)
sum=0
temp2=temp
while temp2>0:               # use another copy
   digit=temp2%10
   sum=sum+(digit**no_of_digits)
   temp2=temp2//10
print("sum of digits of","\"",temp,"\":",sum)
if sum==temp:
    print("----",temp,"is Armstrong number----")
else:
    print("----",temp,"is not Armstrong----")