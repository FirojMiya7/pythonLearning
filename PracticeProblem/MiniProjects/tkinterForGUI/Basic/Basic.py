# Getting Started with Tkinter: Basic Window Creation

import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter Window")
root.geometry("350x500")

root.configure(bg="lightblue")

root.resizable(False, False)

label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 16), bg="lightblue")
label.pack(pady=20)

root.label = tk.Label(root, text="This is a basic window created using Tkinter.", font=("Arial", 12), bg="lightblue")
root.label.pack(pady=10)

root.mainloop()

