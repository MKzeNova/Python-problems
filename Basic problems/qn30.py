n=int(input("Enter your number:"))
factorial=1
if n==0:
    print("factorial: ",1)
elif n<0:
    print("factorial does not exist")
else:
    for i in range(1,n+1):
        factorial*=i
    print("factorial of the number", factorial)