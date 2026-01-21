# Function

# Example of Built In function
"""
a = 9
b = 6
c = sum((a, b))                #Yo ho built in function ctrl + leftClick garesi khulxa

print(c)                        #---> 15 ans aaunxa."""





#User Define Function

#Basic Function
"""
def function1():
    print("This is function 1")
# print(function1())              #--> This is function1 rw next line ma none dekhaunxa...
function1()                       #--> This is function1  . matra Print hunxa"""



#Fucntion take input
"""
def function2(a, b):
    print(f"The sum of {a} and {b} is", a+b)

def function3(a, b):
    average = (a+b)/2
    print(f"The average of {a} and {b} is", average)

function2(3,5)

function3(3,4)                      # yo chai argument pass ko lagi ho

a = int(input("Enter any number:"))
b = int(input("Enter any number:"))

function3(a, b)                    # yo chai user input ko lagi ho"""



#Function with return statement
"""
def function4(a, b):

    # """"""This function is for calculating average of two numbers""""""            #yesari double quete use garera docstring banaucha

    average = (a+b)/2
    print(f"The average of {a} and {b} is", average)
    return average              # return le value farkaunxa jaslai variable ma store garna sakinxa if return nabhaye paar print garda none garxa

avg = function4(4, 7)           # avg variable ma return value store gareko

print(avg)                      # avg variable print gareko

# print(function4.__doc__)                     # yo chai function ko docstring print garxa

# docstring chai kina lekhinxa bhane function ko barema aru le bujhna sajilo hos bhanera ho means documentation ko lagi ho"""