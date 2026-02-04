# Safe Division using try except handling.
"""
Input: two numbers
Handle:
ZeroDivisionError
ValueError
"""

def SafeDivision():
    try:
        num1 = float(input("Enter Numerator: "))
        num2 = float(input("Enter Denominator: "))

        result = num1 / num2
        print(f"Division of Numerator: {num1} and Denominator: {num2} is",result)

    except ZeroDivisionError:
        print("Error: Can not divide by zero!.")
        
    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")


SafeDivision()
