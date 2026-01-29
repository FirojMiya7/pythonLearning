# Scope, Global Variables and the global Keyword

# function bhitra chaii suru ma local variable khojxa if not found bhane global variable khojxa if not found error dinxa

# Local variable
"""
def function1():
    x = 10  # Local variable
    print("Inside function1, x =", x)

function1()
# print(x)  # This will raise an error because x is not defined outside function1
"""


# Global variable (Scooe of global variable is entire file) --> meaning global variable lai file ko kunai pani function bata access garna sakinxa is know as Scope of global variable
"""
def function2():
    global y                                    # Declare y as a global variable    -->  yaha chaii global keyword use garera global variable declare gareko xa jasle garda yedi yespaxi modify bhayo bhani pani global variable ko value pani yespaxi change hunxa
    y = 20                                      # Global variable
    print("Inside function2, y =", y)

function2()
print("Outside function2, y =", y)

# OR Another method to declare global variable

# Modifying a global variable inside a function

z = 30  # Global variable
def function3():
    z = 40                                      # Modify the global variable
    print("Inside function3, z =", z)

function3()
print("Outside function3, z =", z)  # z remains unchanged
# Using the global keyword to modify a global variable
"""


# Passing a global variable as an argument to a function
"""
def function4(n):
    print(n, "\nThis is inside of function4")

function4("Hello World! This is a global variable")  # Passing a global variable as an argument
"""




# Nested functions and global variables
"""
def Feroz():
    x = "Feroz's Local Variable"
    def Sushil():
        x = "Sushil's Local Variable"
        print("'" , x , "'")                                        # Accessing Feroz's local variable from Sushil
    print("Inside Feroz:" , "'" , x , "'")
    Sushil()
    print("Inside Feroz after calling Sushil: " , "'" , x , "'")

Feroz()
"""

# Note: Sushil function cannot be called outside Feroz function as it is local to Feroz function only.