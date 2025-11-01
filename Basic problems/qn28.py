for i in range(25,51):
    if i >1:
        for num in range(2,i):
            if i%num==0:
                break # if this condition become false after checking every numbers from 2 to i-1 , the code will execute from outside of the "if".
        else:
            print(i)
