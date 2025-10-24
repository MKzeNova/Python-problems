#python program to calculate the difference between a given number and 17.If the number is greater than 17 return twice the absolute difference
n=int(input("Enter your number: "))
def dis(c):                                                          # 'dis' is a just a func name that i given, you can use any name, and the c can be any value
    if c>=17:
        return (c-17)*2
    else:
        return (17-c)
a=dis(n) #called the function for the value n
print(a)