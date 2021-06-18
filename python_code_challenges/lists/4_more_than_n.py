"""
4. More Than N.

Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain
type. We have a conveyor belt full of different types of snacks represented by different numbers. Our function will
accept a list of numbers (representing the type of snack), a number for the second parameter (the type of snack we are
looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt).
The function will return True if the snack we are searching for appears more times than we provided as our third
parameter. These are the steps we need:

1. Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number
    of instances
2. Count the number of occurrences of item (the second parameter) in lst (the first parameter)
3. If the number of occurrences is greater than n (the third parameter), return True. Otherwise, return False
"""


# Write your function here

def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
