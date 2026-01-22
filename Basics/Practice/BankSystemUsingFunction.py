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
        print("Insufficient Balance\n")
        return balance
    print("Successfully withdrew!\n")
    return balance - amount
    
def checkBalance(balance):
    """Function to check the current balance"""
    print(f"Your current balance is: {balance}\n")        #or print("your current balance is:" , balance)

balance = 0              #Initial Balance set gareko

while True:
    choice = int(input("\n-----Welcome to Simple Bank System-----\n\nPlease choose:\n1. For Deposit\n2. For Withdraw\n3. For CheckBalance\n4. For Exit\n\nEnter your choice: "))
    
    if choice == 1:
        amt = int(input("Enter your amount to deposit: "))
        balance = deposit(balance, amt)
        print(f"Successfully deposited!\n")
    elif choice == 2:
        amt = int(input("Enter your amount for withdraw: "))
        balance = withdraw(balance, amt)
    elif choice == 3:
        checkBalance(balance)
    elif choice == 4:
        print("Thank you for Choosing Us.")
        break
    else:
        print("Invalid Option. Please try again.\n\n")







# Note: This is a basic implementation and may require additional error handling and input validation for a production-level system.
