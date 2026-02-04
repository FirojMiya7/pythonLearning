# Integer Input Validation using try except and function too.
"""
Keep asking user until valid integer is entered
"""

def IntValidation():
    while True:
        try:
            num = int(input("Enter any integer: "))
            print(f"Input: {num} is valid and integer.")
            break

        except ValueError:
            print("Error: Please input only integer value.")

IntValidation()