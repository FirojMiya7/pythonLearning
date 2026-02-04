# Global Variable Modify
"""
Create global variable count = 0
Function should increase count
"""

count = 0           # yo global variable ho.

def Counter():
    global count            # tells Python we want to use the global variable
    count += 1
    if count == 1:
        print(count, "time called.")
    else:
        print(count , "times called.")

Counter()
Counter()
Counter()                   # jati choti function call hunxa teti choti modify hunxa
















#Just checking after a long time...

"""
var = 32
var1 = "Feroz"

print(type(var), type(var1))
"""