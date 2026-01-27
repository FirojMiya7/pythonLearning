# Opening a file in write mode
# If the file does not exist, it will be created
# If the file exists, its content will be erased
# Writing data to the file
"""
f = open("Basics/Learning/FirojMiya.txt", "w")
f.write("My name is Firoj Miya\n")
f.write("I am learning Python\n")
f.write("I love to code\n")
f.close()
print("File written successfully.\n")
"""


# Add data to the existing file using append mode
"""
f = open("Basics/Learning/FirojMiya.txt", "a")
a = f.write("I am excited to learn more about file handling in Python.\n")            #jati choti run garxam teti choti add hunxa

print(a)  # returns number of characters added | kati characters add bhayo bhanera

f.close()
print("Data appended successfully.\n")
"""




# To read the file, we need to open it in read mode
"""
f = open("Basics/Learning/FirojMiya.txt", "r")
print(f.read())
f.close()
"""