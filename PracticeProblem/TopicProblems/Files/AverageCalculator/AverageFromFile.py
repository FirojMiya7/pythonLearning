# Average Marks
"""
Read marks from existed file
Calculate average
"""



with open("PracticeProblem/TopicProblems/Files/AverageCalculator/Marks.txt", "r") as file:
    totalMarks = 0
    count = 0
    for line in file:
        try:
            marks = int(line.strip())       # line.strip() le line ko suru ra end ma vako whitespace haru hataidinxa
            totalMarks += marks         
            count += 1
        except ValueError:
            print(f"Warning: '{line.strip()}' is not a valid integer and will be skipped.")

    if count == 0:
        print("No valid marks found to calculate average.")
    else:
        average = totalMarks / count
        print(f"Average Marks: {average:.2f}")
                