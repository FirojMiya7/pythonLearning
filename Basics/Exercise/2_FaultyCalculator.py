#Exercise-2    
# Faulty Calculator

#45*3=555 , 56+9=77 , 56/6=4

"""
Design a calculator which will correctly solve all the porblems except the following ones:
45*3=555 , 56+9=77 , 56/6=4
Your program should take operator and the two numbers as input from the user and then return the result
without using funtions
This is for detecting cheaters in exam.
"""

n1=int(input("Enter your First number:"))
op=input("Enter the operation:'+,-,*,/': ")
n2=int(input("Enter your second number:"))

if n1==45 and n2==3 and op=='*':
    print(f"Multiplication of {n1} and {n2} = 555")
elif n1==56 and n2==9 and op=='+':
    print(f"Sumation of {n1} and {n2} = 77")
elif n1==56 and n2==6 and op=='/':
    print(f"Division of {n1} and {n2} = 4")
elif op=='+':
    print(f"Sumation of {n1} and {n2} = ", n1+n2)
elif op=='*':
    print(f"Multiplication of {n1} and {n2} = ", n1*n2)
elif op=='/':
    print(f"Division of {n1} and {n2} = ", n1/n2)
elif op=='-':
    print(f"Subtraction of {n1} and {n2} = ", n1-n2)
else:
    print("Error! Please check your input.")