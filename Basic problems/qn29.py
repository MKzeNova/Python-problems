# Fibonacci series up to 10 terms
a=0
b=1 #in Fibonacci series, each number=sum of two previous numbers, thats why we start with 0 and 1
for i in range(10):
    print(a)
    a = b
    b = a+b
