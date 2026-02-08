# Prime Numbers from File

def primeCheck(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):                   # Check divisibility up to the square root of num --> matlab num ko square root samma nai check garne ho kina bhaney  
        if num % i == 0:
            return False
    return True

with open("PracticeProblem/TopicProblems/Files/ActionByReadFile/Marks.txt", "r") as file:
    primeNumbers = []

    for line in file:
        line = line.strip()
        if not line:
            continue
        try:
            number = int(line)
            if primeCheck(number):
                primeNumbers.append(number)
        except ValueError:
            print(f"Warning: '{line}' is not a valid integer and will be skipped.")

    if primeNumbers:
        print("Prime numbers from the file:")
        for num in primeNumbers:
            print(num)
    else:
        print("No prime numbers found in the file.")