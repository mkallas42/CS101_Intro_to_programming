"""
You are a student and you are trying to organize your subjects and grades using Python.

Let’s explore what we’ve learned about lists to organize your subjects and scores.
"""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# print(gradebook)

gradebook.append(["computer science", 100])

# print(gradebook)

gradebook.append(["visual arts", 93])

# print(gradebook)

gradebook[-1][1] = 93 + 5

# print(gradebook)

gradebook[2][1] = "Pass"

# print(gradebook)

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)
