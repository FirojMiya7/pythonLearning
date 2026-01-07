# Guess The Number
#Like Akinator

n=18                    #My original number value which is hidden for user to guess...

#Take user input
#give hints like its smaller its bigger bla bla
#number of guesses --> 9
#print number of guesses left
#print number of guesses he took to finish
#Game over

guesses=0
max_guesses=9

inp=int(input("\nGuess the number: "))

while(guesses!=max_guesses):
    if inp<n:
        print("\nYour guess is smaller than the number")
        guesses = guesses + 1
        print(f"\nYou have {max_guesses - guesses} guesses left")
        inp = int(input("\nGuess the number: "))
    elif inp>n:
        print("\nYour guess is greater than the number")
        guesses = guesses + 1
        print(f"\nYou have {max_guesses - guesses} guesses left")
        inp = int(input("\nGuess the number: "))
    else:
        print(f"\nYou guessed it right in {guesses} guesses")
        break
    print("Game Over")
    