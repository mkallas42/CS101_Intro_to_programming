"""
4. Dog Years.

Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog
and the age in human years. It will calculate the age of the dog in dog years and return a string describing the
dog’s age. This will require a few steps:

 - Define the function called dog_years to accept two parameters: name and age
 - Calculate the age of the dog in dog years
 - Concatenate the string with the dog’s name and age in dog years
 - Return the resulting string
"""


# Write your dog_years function here:

def dog_years(name, age):
    dog_age = age * 7

    return str(name) + ", you are " + str(dog_age) + " years old in dog years"


# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
