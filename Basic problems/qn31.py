#Reverse a integer number
n=int(input("Enter your number: "))
reversed_no=0
while n >0:
    a=n%10
    reversed_no=reversed_no*10 +a #if there is no '*10' it just gives sum of digits
    n=n//10

print("Reversed number: ",reversed_no)
