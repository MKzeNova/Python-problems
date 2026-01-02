# write a programme to calculate the area of a circle of radius r entered by user

r=float(input("Enter the radius="))
import math
if r==0:
    print("enter a non zero value")
else:

    print("Area of the given circle=",math.pi*r*r)

