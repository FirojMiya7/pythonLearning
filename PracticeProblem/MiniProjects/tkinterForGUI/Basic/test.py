import tkinter as tk
from tkinter import messagebox

def add_student_gui():
    try:
        name = name_entry.get()
        roll = int(roll_entry.get())
        marks = float(marks_entry.get())

        with open("Students.txt", "a") as file:
            file.write(f"{name},{roll},{marks}\n")

        messagebox.showinfo("Success", "Student added successfully")

        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        marks_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Student Management System")
root.geometry("200x250")
root.label = tk.Label(root, text="Add Student", font=("Arial", 14), bg="skyblue")
root.label.pack(pady=10)
root.configure(bg="skyblue")

tk.Label(root, text="Student Name", bg="skyblue").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll Number", bg="skyblue").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Marks", bg="skyblue").pack()
marks_entry = tk.Entry(root)
marks_entry.pack()

tk.Button(root, text="Add Student", bg="#0be394", command=add_student_gui).pack(pady=10)

root.mainloop()



# Baaki paxi garney aahile laii yetti nai dhanyabad.