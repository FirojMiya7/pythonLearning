# Even Numbers from File


with open("PracticeProblem/TopicProblems/Files/ActionByReadFile/Marks.txt", "r") as file:
    evenNumbers = []

    for line in file:
        line = line.strip()
        if not line:
            continue
        try:
            number = int(line)
            if number % 2 == 0:
                evenNumbers.append(number)
        except ValueError:
            print(f"Warning: '{line}' is not a valid integer and will be skipped.")


    if evenNumbers:
        print("Even numbers from the file:")
        for num in evenNumbers:
            print(num)
    else:
        print("No even numbers found in the file.")