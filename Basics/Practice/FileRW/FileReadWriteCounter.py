# Create a file called count.txt.
#Requirements:
"""
Each time the program runs:
Read the number from file
Add 1
Write it back
This simulates:
program remembering how many times it was used
Use:
"r"
"w"
int()
"""


#Implementaion:

try:
    file = open("Basics/Practice/FileRW/count.txt", "r")
    count = int(file.read())
    file.close()
except:
    count = 0

count += 1

file = open("Basics/Practice/FileRW/count.txt", "w")
file.write(str(count))
file.close()

print("File has run ",count,"times.")