"""
1. Every Three Numbers.

Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3
starting from a number that is passed to the function as an input parameter. Here is what we need to do:

1. Define the function to accept one parameter for our starting number
2. Calculate the numbers between the starting number and 100 while incrementing by 3
3. Store the numbers in a list
4. Return the list

The function should return a list of every third number between start and 100 (inclusive). For example,
every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function
should return an empty list.
"""


# Write your function here

def every_three_nums(start):
    if start > 100:
        return []
    else:
        lst = [*range(start, 101, 3)]
    return lst


# Uncomment the line below when your function is done
print(every_three_nums(91))
