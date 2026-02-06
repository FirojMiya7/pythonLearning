# Math Module
# Use sqrt & power

import math

def squareRoot(n):
    SRoot = math.sqrt(n)
    print(f"The Squre root of {n} is", SRoot)

def power(n,i):
    # Power = math.pow(n,i)
    # print(f"{n} to the power of {i} is", Power)

    return math.pow(n,i)


#For Squre
n = int(input("Enter any number: "))
squareRoot(n)


#For Power
i = int(input("\nEnter the power: "))
# power(n,i)
print(f"{n} to the power of {i} is", power(n,i))