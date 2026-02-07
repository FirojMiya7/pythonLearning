# Sum of Digits (of given numbers.)
"""
Input: number
Output: sum of digits
"""

n = int(input("Enter any number: "))
temp = 0

while n > 0:
    temp += n % 10
    n = n // 10                 # '//' for integer division and '/' for float division.

print("The sum of digits of given number is", temp)