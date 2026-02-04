# Global vs Local Test
"""
Same variable name inside & outside function
Print both to see difference
"""


var = 10            # Global variable

def ForLocal():
    var = 5         # Local Variable which is only be access by the function locally..
    print("Inside function var is", var)

ForLocal()

print("Outside function var is", var)