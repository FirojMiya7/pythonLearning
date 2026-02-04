# Even Check
# Lambda returns True/False


CheckEven = lambda x: x % 2 == 0

n = int(input("Enter any number: "))

if CheckEven(n):
    print("True")
    print(f"{n} is even.")
else:
    print("False")
    print(f"{n} is odd.")
