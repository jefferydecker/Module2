"""
Program: cast_to_integer.py - actually mod2topic3casting.py
Author: Jeffery Decker
Last date modified: 08/08/2020

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

rawinput1 = input("Enter something: ")

output = int(float(rawinput1))
print(rawinput1, output)


"""
I found that I first had to cast strings to float, then float to int,
as in line 12, in the case where the input was a float.
In the case of a non-numeric string, I just got an error.
"""
