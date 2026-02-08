# Average Marks
"""
Read marks from file
Calculate average
"""


with open("PracticeProblem/TopicProblems/Files/AverageCalculator/Marks.txt", "a") as file:
    while True:
        try:
            marks = int(input("Enter your Mark: "))
            break
        except ValueError:
            print("Error! Enter integer only.")

    # file.write(marks)                     # marks bhaneko int ho rw file write ko laagi string chayinxa so error show garxa 
    file.write(f"{marks}\n")                # marks lai string ma convert garera file ma write gareko ho kasari bhanda f"{marks}\n" le marks lai string ma convert garda ho ra \n le new line ma write garna help garcha
    print("Your marks added successfully\n")