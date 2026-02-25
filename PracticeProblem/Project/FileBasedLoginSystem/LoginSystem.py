# Project 4: File-based Login System
"""
Requirements:
Username & password store in file
Login check
Wrong input handle
Try/except use garnai parcha

Concepts Used:
file handling
loops
conditions
error handling
"""

# File-based Login System

def readCredentials(filename):
    try:
        with open(filename, "r") as file:
            credentials = {}
            for line in file:
                username, password = line.strip().split(":")
                username = username.lower()  # Convert username to lowercase for case-insensitive login
                credentials[username] = password
            return credentials
    except FileNotFoundError:
        return {}                   # If file not found, return empty dictionary
    

def login(credentials):
    while True:
        try:
            username = input("Enter username: ").lower()
            password = input("Enter password: ")
            
            if not username or not password:
                print("Username and password cannot be empty.")
                continue
            
            if username in credentials and credentials[username] == password:
                print("\n✓ Login successful!")
                return True
            else:
                print("✗ Invalid username or password. Please try again.\n")
        except KeyboardInterrupt:
            print("\nLogin cancelled.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")


# Main execution

if __name__ == "__main__":
    print("===== File-Based Login System =====")
    credentials = readCredentials("PracticeProblem/Project/FileBasedLoginSystem/credentials.txt")
    
    if not credentials:
        print("Error: credentials.txt not found!")
    else:
        if login(credentials):
            print("\nWelcome to the system!")
        else:
            print("Login failed.")