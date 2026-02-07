# Reverse Number
"""
Input: integer
Output: reversed number
"""

n = int(input("Enter any number: "))
rev = 0

while n > 0:
    lastDigit = n % 10
    rev = rev * 10 + lastDigit
    n = n // 10                     # Double slash for integer and single slash for float division

print("After Reversed:", rev)