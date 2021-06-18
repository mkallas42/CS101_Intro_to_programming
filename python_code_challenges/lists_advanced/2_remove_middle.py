"""
2. Remove Middle.

Our next function will remove all elements from a list with an index within a certain range. The function will accept
a list, a starting index, and an ending index. All elements with an index between the starting and ending index should
be removed from the list. Here are the steps:

1. Define the function to accept three parameters: the list, the starting index, and the ending index
2. Get all elements before the starting index
3. Get all elements after the ending index
4. Combine the two partial lists into the result
5. Return the result

The function should return a list where all elements in lst with an index between start and end (inclusive) have
been removed.

For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
"""