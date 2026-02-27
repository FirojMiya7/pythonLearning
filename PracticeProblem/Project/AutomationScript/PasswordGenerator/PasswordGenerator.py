# Project 6: Automation Script (Real Power 🔥)
"""
Option B: Password Generator
Random password generate
length user input
save to file
"""

def GeneratedPassword(length):
    import random
    import string

    characters = string.ascii_letters + string.digits + string.punctuation      # ascii_letters: a-zA-Z, digits: 0-9, punctuation: special characters where space is not included
    password = ''.join(random.choice(characters) for _ in range(length))        
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer for password length.")
            return
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    password = GeneratedPassword(length)
    print(f"Generated Password: {password}")

    try:
        with open("PracticeProblem/Project/AutomationScript/PasswordGenerator/Passwords.txt", "a") as file:
            file.write(password + "\n")
    except Exception as e:
        print(f"Error saving password to file: {e}")

if __name__ == "__main__":
    main()
        