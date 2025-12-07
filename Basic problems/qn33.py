#create a function that accepts a variable number of arguments and prints each of their values.
def print_values(*args):
    print("printing values:")
    for i in args:
        print(i)
print_values(10,2,20,4,30,6)