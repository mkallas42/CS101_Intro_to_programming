"""
3. Max Num.

Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of
numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually
implement this function. Here is what we need to do:

 - Define the function to accept a list of numbers called nums
 - Set our default maximum value to be the first element in the list
 - Loop through every number in the list of numbers
 - Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
 - Return the maximum number
"""


# Write your function here

def max_num(nums):
    maximum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num
    return maximum


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
