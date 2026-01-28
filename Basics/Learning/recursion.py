#Recursion
# A recursive function is a function that calls itself in order to solve a problem.

#Factorial of a number using recursion
"""
parameter : n : integer
return : n * n-1 * n-2 * n-3 * ........*1
"""
"""
n! = n * n-1 *n-2 * n-3 * ........*1
or
n! = n * (n-1)!
"""

#Implementation:

# Method 1: Using iterative approach
"""
def factorial(n):
    fact = 1
    for i in range(n):              # i 0 dekhi n number samma
        fact = fact * (i+1)         # i+1 kina bhaney i suru ma 0 hunxa so 0 mul always 0
    return fact                     # last ma ans return garxa

number = int(input("Enter a number to find its factorial: "))

print("Factorial using iterative method of ",number,"is", factorial(number))
"""


# Method 2: Using recursive approach
"""
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

number = int(input("Enter a number to find its factorial: "))

print("Factorial using recursive method of",number,"is", factorial(number))
"""