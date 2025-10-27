# program to compute the sum of digits of a number using recursion.
def sum_of_digits(a):
    if a==0:
        return 0
    else:
        if a>0:
            return (a%10)+ sum_of_digits(a//10)
n=int(input("Enter your number: "))
print("sum of digits of",n,"= ",sum_of_digits(n))

