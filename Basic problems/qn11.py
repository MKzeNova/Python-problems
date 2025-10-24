# program that computes the greatest common divisor/ highest common facor(HCF) of two positive integers
def hcf(x,y):
    if x%y==0:
        return y
    for i in range(int(y),0,-1):
        # y might be a float, so int() ensures it’s converted to an integer.
        # The HCF (Highest Common Factor) of two numbers can never be greater than the smaller number (y in this case).
        
        #In fact, it also can’t be greater than half of that smaller number — except when one number divides the other exactly.but here i didn't applied that, ie y/2

        if x%i==0 and y%i==0:
            a=i
            return a
n1=int(input("Enter your first no. "))
n2=int(input("Enter your second no. "))
var=hcf(n1,n2) 
print(var,"is the hcf")