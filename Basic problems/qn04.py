#a script that calculates n+nn+nnn but allows the user to input any number of repetitions.
a=int(input("enter the integer: "))
n1=int(str(a)*int(input("enter the 1st rept value")))
n2=n=int(str(a)*int(input("enter the 2nd rept value")))
n3=int(str(a)*int(input("enter the 3rd rept value")))
print(n1+n2+n3)