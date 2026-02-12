# Tail Recursive Sum of N Numbers


def TailSum(n, acc = 0):
    if n == 0:
        return acc
    else:
        return TailSum(n -1, acc + n)
    
# Example usage
number = 5              # 1+2+3+4+5 = 15 

# Or you can take input from user
# number = int(input("Enter a number: "))

print(f"Sum of first {number} natural numbers is: {TailSum(number)}")