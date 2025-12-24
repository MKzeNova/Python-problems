#Calculate and print the sum and average of all numbers in a given list
#list=[10,20,30,40,50]

list=[10, 20, 30, 40, 50]

sum=0
for element in list:
    sum=sum+element
print("sum of elements:",sum)

no_of_elements=len(list)
avg=sum/no_of_elements
print("average of elements of the list:",avg)
