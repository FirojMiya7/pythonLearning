# Write Names to File
"""
Take name from user
Save to file
"""

file = open("PracticeProblem/TopicProblems/Files/WriteReadFile/Name.txt", "w")

name = input("Enter Your name: ")

file.write(name)
print("Name successfully written to the file.\n")

file.close


