# Pattern Printing Exercise

# Write a Python program to print the following pattern:

# input = integer (n)
# output = pattern:
# Boolean = (check by input 1 or 0) also typecast later that it is boolean variable

"""
True
*
**
***
****

False
****
***
**
*"""


#Implementation:

try:
    while True:
        n = int(input("Enter any number to build pattern: "))
        patternType = int(input("Enter pattern type 1 or 0: "))

        if patternType == 1:
            boolean = bool(patternType)
            print(boolean)
            for i in range(1, n + 1):
                print("*" * i)

        elif patternType == 0:
            boolean = bool(patternType)
            print(boolean)
            for j in range(n, 0, -1):
                print("*" * j)

        else:
            print("Invalid pattern type! Only 0 or 1 allowed.")
            continue

        choice = int(input("Enter 3 to exit or any other number to continue: "))
        if choice == 3:
            print("Thank you for using our pattern program.")
            break

except ValueError:
    print("Error: Please enter only integer values!")

