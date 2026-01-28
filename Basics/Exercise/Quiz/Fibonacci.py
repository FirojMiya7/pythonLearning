#Fibonacci Series:
# Example: 0 1 1 2 3 5 8 13 and so on

# Implementation:

# Yesley just tyo index ma bhako value matra diyo but
"""
def Fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

number = int(input("Enter a number upto you want to continue your fibonacci series: "))

print("Fibonacci series:\n",Fibonacci(number))
"""

# But malai purai series form maii chaiyo then..

# Method 2: Using iterative approach
"""
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibSeries = [0,1]
        for i in range(2, n):
            fibSeries.append(fibSeries[i-1] + fibSeries[i-2])               # .append le list ko last ma naya element add garcha
        return fibSeries

number = int(input("Enter a number upto you want to continue your fibonacci series: "))

print("\nFibonacci Series: ",fibonacci(number),"\n")
"""


# Method 3: Fibonacci series upto a given limit i.e. if 7 is given then series will be 0 1 1 2 3 5 -> 6 ota.
"""
def fibonacci(limit):
    fibSeries = [0,1]
    while True:
        nextValue = fibSeries[-1] + fibSeries[-2]               # [-1] le last element dinxa ani [-2] le second last element dinxa list ko property ho yo 
        if nextValue > limit:
            break
        else:
            fibSeries.append(nextValue)

    return fibSeries

number = int(input("Enter Limit: "))
print("Fibonacci Series: ", fibonacci(number))
"""
# Method 4: Fibonacci series using generator function
"""
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a                     # yield le generator function banauxa yo return jasto ho tara yo function ko state lai pani save garcha
        a, b = b, a + b
number = int(input("Enter Limit: "))
print("Fibonacci Series: ", list(fibonacci(number)))    # list() le generator function ko sabai values lai list ma convert garcha and print garcha
"""