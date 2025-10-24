#program to convert height in feet and heiht in  inches to centimeters.
print("Input your Height in")
hfeet=int(input("feet: "))
hinch=int(input("inches: "))
H=hfeet+(hinch/12)
hcm=H*30.48
print(f"Your height in cm is = {hcm}") # 'f {} ' are used to easily insert variables or expressions inside strings. Just to make look cleaner and easy
      