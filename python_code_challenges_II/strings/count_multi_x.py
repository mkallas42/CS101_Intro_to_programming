"""
3. Count Multi X.

Now let’s change our function to compare against an entire string instead of a single character. This function should
accept a string and a substring to compare against. The number of occurrences of the second parameter within the first
parameter string are returned. What this means is that we are checking the number of occurrences of the shorter string
(second parameter) within the longer string (first parameter). One way to accomplish this is using the split function.
Here is how to do that:

 - Define the function to accept two parameters. word for the input string and x for the second string we are
 searching for
 - Split the string into substrings based on the second input parameter
 - Count the number of instances the substring appeared in the first input string based on the split string
 - Return the result
"""


# Write your count_multi_char_x function here:

def count_multi_char_x(word, x):
    splits = word.split(x)
    return len(splits) - 1


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
