# Tail Recursive GCD (Important for exam 🔥)

# GCD (Greatest Common Divisor) of two numbers can be calculated using the Euclidean algorithm, which can be implemented in a tail recursive manner.

def TailGCD(a, b):
    if b == 0:
        return a
    else:
        return TailGCD(b, a % b)

# Example usage
num1 = 48
num2 = 18
# Or you can take input from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is: {TailGCD(num1, num2)}")