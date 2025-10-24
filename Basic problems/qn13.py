#  program that returns true if the two given integer values are equal or their sum or difference is 5.
a=int(input("enter your first number: "))
b=int(input("enter your second number: "))
if a==b or a+b==5 or abs(a-b)==5: # abs make a-b always positive
    print("True")
else:
    print("False")