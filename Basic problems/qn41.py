# programme to check if a triangle (using functions, side lengths are entered by user ) is right triangle or not
def is_right_triangle(a,b,c):
    if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:   # Pythagoras theorem
        print("---Right triangle---")
    else:
        print("---Not right triangle---")
side1=int(input("Enter side length1:"))
side2=int(input("Enter side length2:"))
side3=int(input("Enter side length3:"))

is_right_triangle(side1,side2,side3)
