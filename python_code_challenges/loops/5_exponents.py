"""
5. Exponents.

In this challenge, we will be using nested loops in order to raise a list of number to the power of a list of other
numbers. What this means is that for every number in the first list, we will raise that number to the power of every
number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then
there will be 6 final answers. Let’s look at the steps we need:

 - Define the function to accept two lists of numbers, bases and powers
 - Create a new list that will contain our answers
 - Create a loop that iterates through every base in bases
 - Within that loop, create another loop that iterates through every power in power
 - Within that nested loop, append the result of the current base raised to the current power.
 - After all iterations of both loops are complete, return the list of answers
"""


# Write your function here

def exponents(bases, powers):
    expo_lst = []

    for base in bases:
        for power in powers:
            expo_lst.append(base ** power)
    return expo_lst


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
