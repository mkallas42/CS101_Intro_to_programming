"""
1. Larger Sum.

We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum.
We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which
one has a greater sum. Here are the steps we need:

 - Define the function to accept two input parameters: lst1 and lst2
 - Create two variables to record the two sums
 - Loop through the first list and add up all of the numbers
 - Loop through the second list and add up all of the numbers
 - Compare the first and second sum and return the list with the greater sum
"""


# Write your function here

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0

    for num in lst1:
        sum1 += num

    for num in lst2:
        sum2 += num

    if sum1 >= sum2:
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))