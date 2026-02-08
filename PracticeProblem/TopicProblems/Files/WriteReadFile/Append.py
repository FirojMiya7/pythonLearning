# Append Data

# Append new data without deleting old



with open("PracticeProblem/TopicProblems/Files/WriteReadFile/Name.txt", "a") as file:
    addData = input("Enter another name: ")
    file.write("\n" + addData)
    print("Element successfully added to the file.\n")