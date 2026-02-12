# Tail Recursive Factorial

# helper variable (accumulator) use 


def TailFacto(n, acc = 1):
    if n == 0:
        return acc
    else:
        return TailFacto(n - 1, acc * n)

# Example usage
number = 5
print(f"Factorial of {number} is: {TailFacto(number)}")
    