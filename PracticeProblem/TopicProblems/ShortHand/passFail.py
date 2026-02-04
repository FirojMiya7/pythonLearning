# To check if a student pass or fail based on marks obtained

marks = int(input("Enter your obtained marks: "))

print(f"Your are Pass with {marks} marks." if marks >= 40 else f"Fail! Better luck next time.\nMarks:{marks}")