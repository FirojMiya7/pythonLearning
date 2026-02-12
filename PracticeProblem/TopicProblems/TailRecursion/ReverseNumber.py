# Tail Recursive Reverse Number

def TailReverse(n , rev = 0):
    if n == 0:
        return rev
    else:
        rev = rev * 10 
        rev += n % 10
        return TailReverse(n // 10, rev)

# Example usage
number = 12345

# Or you can take input from user
# number = int(input("Enter a number: "))

print(f"Reverse of {number} is: {TailReverse(number)}")

