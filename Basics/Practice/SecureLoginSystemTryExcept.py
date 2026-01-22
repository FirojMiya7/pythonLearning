#Secure Login System with Try-Except

# Requirements:
"""
1. Correct username = "admin"
2. Correct password = "1234"
3. User lai 3 attempts dinxa to enter correct credentials.
4. If user enters correct credentials within 3 attempts, print "Login Successful", and exit the program.
5. If user fails to enter correct credentials in 3 attempts, print "Account Locked".
6. Use try-except to handle Empty inputs.
"""


# Implementation:

username = "admin"
password = "1234"

attempts = 3

while attempts > 0:
    try:
        user = input("Enter username:")
        pwd = input("Enter password:")
        if not user or not pwd:
            raise ValueError("Empty input is not allowed.")
        if user == username and pwd == password:
            print("Login Successful")
            break
        else:
            attempts -= 1
            print(f"Incorrect credentials. You have {attempts} attempts left.\n")
    except ValueError as ve:
        print(ve)
        attempts -= 1
        print(f"You have {attempts} attempts left.\n")
if attempts == 0:
    print("Account Locked")
