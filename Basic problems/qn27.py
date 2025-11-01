#  Python program to display only those numbers from a list that satisfy the following conditions
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the following number
#If the number is greater than 500, then stop the loop
list=[12, 75, 150, 180, 145, 525, 50] .
for i in list:
    if i>500:
        break #break stops the entire loop immediately.The loop ends here no further numbers are checked.
    elif i>150:
        continue  #Meaning of continue:It skips the rest of the code inside the loop for this iteration and moves to the next number.
        print("hI")
    elif i%5==0:
        print(i)

#output 75 150 145

     

