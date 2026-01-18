#take a user input for example 356 dexa bhani output ma 3 ani next line ma 5 ani next line 6 huna paryo hana
"""
num = input("Enter any number: ")

index = 0
while index < len(num):
    print(num[index])
    index += 1"""



#OR

#another method
"""
num = input("Enter any number: ")           
for x in num:
    print(x)"""



#aahile samma tw input ligda string ma lirathyo aaba maile integer ma lina paryo bhani k 
# garney kasari change garney?




# Method 1 - int() then str() (complicated)
"""
num = int(input("Enter any number: "))
num = str(num)

index = 0
while index < len(num):
    print(f"{index+1}:",num[index])
    index += 1"""


# Method 2 - int() then str() (complicated)
"""
num = int(input("Enter any number: "))
for x in str(num):
    print(x)"""