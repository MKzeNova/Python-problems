# write a programme for recursive multiplication two positive integers
def multiply(a,b):
    if b==0:
        return 0
    else:
        return a+ multiply(a, b-1)   #remember, multiplication means repeated addition,For example:
                                     # 5 × 3 = 5 + 5 + 5
                                     # So, if multiply(a, b) means "add a exactly b times".
n1=int(input("First positive number="))
n2=int(input("Second positive number="))
print("result=",multiply(n1,n2))