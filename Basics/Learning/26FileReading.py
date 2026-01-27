# Read from a file
"""
f = open("Basics/Learning/Feroz.txt", "r")                  # yaha f bhaneko pointer ho file ko exactly pointer pani haina file handling garna ko lagi ho
content = f.read()
print(content)
f.close()
"""



#Read specific number of characters
"""
f = open("Basics/Learning/Feroz.txt", "r")
content = f.read(4)                 #Read first 4 characters
print(content)

content = f.read(4)                 #After reading 4 more characters
print(content)
f.close()
"""



# Read line by line
"""
f = open("Basics/Learning/Feroz.txt", "r")

#### Print All the characters line by line 

# content = f.read()
# for line in content:
#     print(line)
# f.close()


#### Print line by line
for line in f:
    print(line , end="")          # to avoid double new line
f.close()
"""



# Read line by line using readline()
"""
f = open("Basics/Learning/Feroz.txt", "r")
print(f.readline(),)             # Read first line
print(f.readline(), end="")      # Read second line --> end = "" is to avoid double new line
print(f.readline(), end="")      # Read third line
f.close()
"""



#Read all lines using readlines()
"""
f = open("Basics/Learning/Feroz.txt", "r")

# method 1
# content = f.readlines()          # Read all lines and store them in a list
# print(content)

# method 2
# print(f.readlines())            # Print all lines as a list??

# method 3
# for line in f.readlines():        # Read all lines one by one
#     print(line, end="")          # to avoid double new line

f.close()
"""