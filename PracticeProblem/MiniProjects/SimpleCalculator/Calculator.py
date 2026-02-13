# Project 2: Simple Calculator

# Requirements:
"""
Menu driven calculator with the following operations:
- Add
- Subtract
- Multiply
- Divide

Error handling for:
- Invalid input
- Division by zero
- Loop until user exits
"""

def Add():
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"Result: {result}\n")
    except ValueError:
        print("Error! Invalid input. Please enter a valid number.\n")

def Subtract():
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"Result: {result}\n")
    except ValueError:
        print("Error! Invalid input. Please enter a valid number.\n")

def Multiply():
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"Result: {result}\n")
    except ValueError:
        print("Error! Invalid input. Please enter a valid number.\n")

def Divide():
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error! Cannot divide by zero.\n")
            return
        result = num1 / num2
        print(f"Result: {result}\n")
    except ValueError:
        print("Error! Invalid input. Please enter a valid number.\n")

def main():
    while True:
        print("\n" + "-" * 5 + " Simple Calculator " + "-" * 5)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            Add()
        elif choice == "2":
            Subtract()
        elif choice == "3":
            Multiply()
        elif choice == "4":
            Divide()
        elif choice == "5":
            print("Thank you for using Simple Calculator!")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 5.\n")


main()