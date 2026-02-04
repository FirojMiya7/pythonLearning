# Factorial using Recursion Function

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
    
n = int(input("Enter positive number for factorial: "))

print(f"The factorial of {n} is", factorial(n))