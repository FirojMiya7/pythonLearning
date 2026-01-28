#Health Management System

# 3 clients - 1. Feroz 2. Sushil 3. Trishan
#Requirements:
"""
use this function:
def getdate():
    import datetime
    return datetime.datetime.now()

1. Total 6 files:
    a. 3 files for exercise
    b. 3 files for diet
2. Write a function that when executed takes as input client name and log type (exercise or diet).
[timestamp here] -> log value
3. One more function to retrieve exercise or diet for any client.

so final 
first ma ask garxa log garney ho ki retrieve garney ho?
then kasko garney ho?
then exercise ho ki diet ho?
print message accordingly
  """  
#Solution:

def getdate():
    import datetime
    return datetime.datetime.now()

print("---------- Welcome to Health Management System ----------\n")

clientList = {1: "Feroz", 2: "Sushil", 3: "Trishan"}
logList = {1: "Exercise", 2: "Diet"}

takeInput = int(input("Press 1 to log the value and 2 to retrieve the value: "))

if takeInput == 1:
    clientChoice = int(input("Select the client: 1 for Feroz, 2 for Sushil, 3 for Trishan: "))
    logChoice = int(input("Select the log type: 1 for Exercise, 2 for Diet: "))

    with open(f"Basics/Exercise/File/txtFiles/{clientList[clientChoice]}_{logList[logChoice]}.txt", "a") as f:
        value = input(f"Enter the {logList[logChoice]} details: ")
        f.write(f"[{getdate()}]: {value}\n")
    print("Log has been recorded successfully.")

elif takeInput == 2:
    clientChoice = int(input("Select the client: 1 for Feroz, 2 for Sushil, 3 for Trishan: "))
    logChoice = int(input("Select the log type: 1 for Exercise, 2 for Diet: "))

    try:
        with open(f"Basics/Exercise/File/txtFiles/{clientList[clientChoice]}_{logList[logChoice]}.txt", "r") as f:
            content = f.read()
            if content:
                print(f"\n{logList[logChoice]} logs for {clientList[clientChoice]}:")
                print(content)
            else:
                print("No logs found.")
    except FileNotFoundError:
        print(f"No {logList[logChoice].lower()} logs found for {clientList[clientChoice]}.")

else: 
    print("Invalid Input!")

