#Find the largest item from the list user created
list=[]
no_of_elements=int(input("Enter number of elements of list:"))
for i in range(0,no_of_elements):
    element=int(input("Enter the element:"))
    list.append(element)
print(list)
print("The largest item from the list is ",max(list))