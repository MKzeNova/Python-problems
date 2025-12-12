# Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.
#If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.
def sort_numbers(numbers, order_type):
    if order_type == "asc":
        return sorted(numbers)
    elif order_type == "desc":
        return sorted(numbers, reverse=True)
    elif order_type == "none":
        return numbers
    else:
        return "Invalid order type"
