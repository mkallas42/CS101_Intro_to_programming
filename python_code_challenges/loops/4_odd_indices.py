"""
4. Odd Indices.

This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as
an input parameter and loop through the odd indices instead of the elements. Here are the steps needed:

 - Define the function header to accept one input which will be our list of numbers
 - Create a new list which will hold our values to return
 - Iterate through every odd index until the end of the list
 - Within the loop, get the element at the current odd index and append it to our new list
 - Return the list of elements which we got from the odd indices.
"""


# Write your function here

def odd_indices(lst):
    odd_lst = []
    for num in range(1, len(lst), 2):
        odd_lst.append(lst[num])
    return odd_lst


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
