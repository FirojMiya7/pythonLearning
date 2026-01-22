#Simple Bank System Using Functions (Practice)

#Requirements:
"""
1. System ma Initial Balance 0 hunxa
2. User le options choose garna sakinxa:
    a. Deposit Money
    b. Withdraw Money
    c. Check Balance
    d. Exit
3. Deposit function: Balance ma amount add garney
4. Withdraw function:
    a. Balance bata amount subtract garney
    b. Withdraw amount balance bhanda thulo bhaye error message dekhauney
5. Check Balance function: Current balance print garney
6. Exit function: Program terminate garney
7. Invalid option handle garney
"""


#Implementation:

def deposit(balance,amount):
    """Function to deposit money into the account"""
    return balance + amount

def withdraw(balance, amount):
    """Function to withdraw money from the account"""
    if amount > balance:
        print("Insufficient Balance")
        return balance
    return balance - amount
    
def checkBalance(balance):
    """Function to check the current balance"""
    print(f"Your current balance is: {balance}")        #or print("your current balance is:" , balance)

balance = 0

choice = int(input("Please choose:\n1. For Deposit\n2. For Withdraw\n3. For CheckBalance\n4. For Exit"))

while True:
    if choice == 1:
        amt = int(input("Enter your amount to deposit:"))
        balance = deposit(balance, amt)
    elif choice == 2:
        amt = int(input("Enter your amount for withdraw:"))
        balance = withdraw(balance, amt)
    elif choice == 3:
        balance = checkBalance(balance)
    elif choice == 4:
        print("Thank you for Choosing Us.")
        break
    else:
        print("Invalid Option. Please try again.")
    # choice = input("Please choose:\n1. For Deposit\n2. For Withdraw\n3. For CheckBalance\n4. For Exit")







# Note: This is a basic implementation and may require additional error handling and input validation for a production-level system.
