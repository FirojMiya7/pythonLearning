# Random Guess Game
"""
Computer generates random number (1–10)
User guesses until correct
"""


import random

# num = random.randrange(1,10)                    # possible output: 1 2 3 4 5 6 7 8 9 (last ko exclude garxa)
num = random.randint(1,10)                      # possible output: 1 2 3 4 5 6 7 8 9 10 (last ko include garxa)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess == num:
            print("\nCongratulations! You guessed it correct.")
            if attempts == 1:
                print(f"It took you {attempts} attempt.")
            else:
                print(f"It took you {attempts} attempts.")
            print("Hope you enjoyed the game.")
            break

        elif guess < num:
            print("You guessed little lower, Try again!\n")

        elif guess > num:
            print("You guessed little higher, Try again!\n")

    except ValueError:
        print("Error! please input integer only.\n")