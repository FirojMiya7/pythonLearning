# Fibonacci Series using Recursion
"""
Print first n fibonacci numbers
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter number for Fibonacci Series: "))

print(f"Fibonacci Series:", fibonacci(n))       # yesle sirf value sum gareko matra dinxa 

#But we need in series.

for i in range (n):
    print(fibonacci(i), end=" ")