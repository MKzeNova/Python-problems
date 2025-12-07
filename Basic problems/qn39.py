#a recursive function to calculate the factorial of 5
def factorial(a):
    if a==0:        #The function needs a condition to stop calling itself.ie base case, here this if condition is the base case
        return 1
    return a*factorial(a-1)
print(factorial(5))
