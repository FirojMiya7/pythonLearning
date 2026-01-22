# Try_Except block is used to handle errors in Python. 
# It allows you to write code that can gracefully handle exceptions without crashing the program.


# Taking two inputs from the user
"""
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    result = int(num1) + int(num2)
    print("The sum of two numbers is:", result)
    
except Exception as e:
    print("The error is:", e)"""


# Using function to handle exceptions
"""
def get_number(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Number matra halnu hos")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

print("Sum =", num1 + num2)
"""