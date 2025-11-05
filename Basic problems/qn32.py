# print elements present in the odd positions of the given list
my_list=[1,2,3,4,5,6,6,7,8,8,8,8,9]
for i in my_list[1: :2]: # means, index[start:stop:step]
    print(i,end=",")
