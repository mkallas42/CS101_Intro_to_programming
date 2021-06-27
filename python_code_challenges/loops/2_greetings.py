"""
2. Greetings.

You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function
to accomplish this task for us. In this challenge, we will take a list of names and prepend the string 'Hello, '
before each name. This will require a few steps:

 - Define the function to accept a list of strings as a single parameter called names
 - Create a new list of strings
 - Loop through each name in names
 - Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
 - Afterwards, return the new list of strings
"""


# Write your function here

def add_greetings(names):
    lst = []
    for name in names:
        lst.append("Hello, " + name)
    return lst


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
