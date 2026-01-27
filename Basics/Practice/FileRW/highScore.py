# Make a file called: highscore.txt
"""
Each time the program runs:
Ask user to enter their score
Read old high score from file
If new score is higher → save it
Otherwise keep the old one
Print the high score
This is how real games store scores 🎮
"""


try:
    file = open("Basics/Practice/FileRW/highscore.txt", "r")
    HS = int(file.read())
    file.close()
except:
    HS = 0

Score = int(input("Enter your Score: "))
if Score > HS:
    file = open("Basics/Practice/FileRW/highscore.txt", "w")
    file.write(str(Score))
    file.close()
    print("Congratulation! You broke the last Record.")
    print("The new record is", Score)
else:
    print("Better Luck Next Time!\n")
    print("The HighScore yet is ", HS)