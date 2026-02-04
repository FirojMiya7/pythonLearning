# Add Using Lambda
# Lambda to add two numbers

add = lambda x , y: x + y

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(f"Sum of {n1} and {n2} is", add(n1,n2))