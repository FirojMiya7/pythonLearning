# Project 1: Student Management System

# Requirements:
"""
Menu-based program

# Options:
Add student (name, roll, marks)
View all students
Exit

Store data in file

# Use:
functions
loops
try/except
with-block
"""



def AddStudent():
    try:
        name = input("\nEnter student name: ")
        roll = int(input("Enter student roll number: "))
        marks = float(input("Enter student marks: "))
        
        with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "a") as file:
            file.write(f"{name},{roll},{marks}\n")
    except ValueError:
        print("Error! Invalid input. Roll must be an integer and marks must be a number.\n")
         
         
def UpdateStudent():
    try:
        UpdateRoll = int(input("\nEnter the roll number of the student to update: "))
        found = False
        
        with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "r") as file:
            students = file.readlines()
            with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "w") as file:
                for student in students:
                    name, roll, marks = student.strip().split(",")
                    if int(roll) == UpdateRoll:
                        new_name = input("Enter new name: ")
                        new_marks = float(input("Enter new marks: "))
                        file.write(f"{new_name},{roll},{new_marks}\n")
                        print(f"Student with roll number {UpdateRoll} has been found and updated successfully.\n")
                        found = True
                    else:
                        file.write(student)

        if not found:
            print(f"Student with roll number {UpdateRoll} has not been found.\n")
    except ValueError:
        print("Error! Invalid input. Roll must be an integer and marks must be a number.\n")
                
        
def ViewStudents():
    try:
        with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No students found.\n")
                return
            
            print("\n" + "-" * 5 + " Student List " + "-" * 5 + "\n")
            for student in students:
                name, roll, marks = student.strip().split(",")
                print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
    except FileNotFoundError:
        print("No Students file found. The file does not exist.\n")
                
        
def AverageMarks():
    try:
        with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No students found to calculate average marks.\n")
                return
            
            TotalMarks = 0
            for student in students:
                name, roll, marks = student.strip().split(",")
                TotalMarks += float(marks)
            
            AvgMarks = TotalMarks / len(students)
            print(f"\nAverage Marks of all students: {AvgMarks:.2f}\n")         # :.2f is used to format the average marks to 2 decimal places.
    except FileNotFoundError:
        print("No Students file found. The file does not exist.\n")
        
        
def SearchStudent():
    try:
        SearchRoll = int(input("\nEnter the roll number of the student to search: "))
        found = False
        
        with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "r") as file:
            students = file.readlines()
            for student in students:
                name, roll, marks = student.strip().split(",")
                if int(roll) == SearchRoll:
                    print(f"Student found: \nName: {name}, Roll: {roll}, Marks: {marks}\n")
                    found = True
                    break
        
        if not found:
            print(f"Student with roll number {SearchRoll} has not been found.\n")
    except ValueError:
        print("Error! Invalid input. Roll must be an integer.\n")
                

def DeleteStudent():
    try:
        DeleteRoll = int(input("\nEnter the roll number of the student to delete: "))
        found = False
        
        with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "r") as file:
            students = file.readlines()
            with open("PracticeProblem/MiniProjects/StudentManagementSystem/Students.txt", "w") as file:
                for student in students:
                    name, roll, marks = student.strip().split(",")
                    if int(roll) == DeleteRoll:
                        print(f"Student with roll number {DeleteRoll} has been found and deleted successfully.\n")
                        found = True
                        continue                    
                    else:
                        file.write(student)

        if not found:
            print(f"Student with roll number {DeleteRoll} has not been found.\n")
                        
    except ValueError:
        print("Error! Invalid input. Roll must be an integer.\n")
        
        
def main():
    while True:
        print("\n" + "-" * 5 + " Student Management System " + "-" * 5)
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Average Marks")
        print("5. Search Student")
        print("6. Update Student")
        print("7. Exit\n")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            AddStudent()
        elif choice == 2:
            ViewStudents()
        elif choice == 3:
            DeleteStudent()
        elif choice == 4:
            AverageMarks()
        elif choice == 5:
            SearchStudent()
        elif choice == 6:
            UpdateStudent()
        elif choice == 7:
            print("\nExiting the system.\nThank you for using the Student Management System!\n")
            break
        else:
            print("Error! Invalid choice. Please try again.\n")
            
            
            
main()
