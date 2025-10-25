# program to calculate sum of digits of a number.
n=int(input("Enter your number : ")) #loop variable initialisation
sum=0
i=n # i used n as i in loop for display the n at last
while i>0: # condition for while loop termination,here loops works until n<0
    a=i%10
    sum+=a
    i=i//10 # loop variable initialisation
print(f"sum of digits of \"{n}\" = {sum}")


