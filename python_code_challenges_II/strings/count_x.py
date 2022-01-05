"""
2. Count X.

Next, we are going to try something a bit different. This time we are going to count the number of occurrences of a
certain letter within a string. Our function will accept a parameter for a string and another for the character which
we are going to count. For example, providing the word "mississippi" and the character 's' would result in an answer
of 4. These are the steps we need to take:

 - Define the function to accept two parameters. word for the input string and x for the single character
 - Create a counter to keep track of the occurrences
 - Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
 - Return the counter after looping through the entire string.
"""


# Write your count_char_x function here:

def count_char_x(word, x):
    letter_count = 0
    for letter in word:
        if x == letter:
            letter_count += 1
    return letter_count


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
