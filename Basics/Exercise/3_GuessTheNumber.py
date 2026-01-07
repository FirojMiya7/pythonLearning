# Guess The Number
#Like Akinator

n=18                    #My original number value which is hidden for user to guess...

#Take user input
#give hints like its smaller its bigger bla bla
#number of guesses --> 9
#print number of guesses left
#print number of guesses he took to finish
#Game over

guesses = 1
max_guesses = 9
won = False

inp = int(input("\nGuess the number: "))

while guesses < max_guesses:
    if inp < n:
        print("\nYour guess is smaller than the number")
    elif inp > n:
        print("\nYour guess is greater than the number")
    else:
        print(f"\nYou guessed it right in {guesses} guesses")
        won = True
        break
    
    guesses += 1
    print(f"You have {max_guesses - guesses} guesses left")
    inp = int(input("\nGuess the number: "))

# Check final guess if loop ended naturally
if not won and inp == n:                #yaha samma tw won still false xa ni tw last guess ho yo.
    print(f"\nYou guessed it right in {guesses} guesses")
    won = True

if not won:
    print(f"\nGame Over! The number was {n}")
    print("Better luck next time!")
    