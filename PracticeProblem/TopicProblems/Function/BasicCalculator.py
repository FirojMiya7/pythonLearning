# Basic Calculator Functions
"""
Create functions:
add(a, b)
sub(a, b)
mul(a, b)
div(a, b)
Each function should return value
"""


def add(a,b):
    result = a+b
    return result

def sub(a,b):
    result = a-b
    return result

def mul(a,b):
    result = a*b
    return result

def div(a,b):
    result = a/b
    return result

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Your sum is ",add(a,b))
print("Your sub is ",sub(a,b))
print("Your mul is ",mul(a,b))
print("Your div is ",div(a,b))

"""
check = add(a,b*2)
print(check)        #result --> 9 when a = 5 and b = 2.
"""