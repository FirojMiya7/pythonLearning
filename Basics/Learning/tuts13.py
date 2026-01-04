"""
If else , elif conditions
"""


var1 = 26
var2 = 54

var3 = int(input("Enter any Number: "))
if var3==var2:
    print(f"{var3} is equal to {var2}")
elif var3>var2:                                         #yesma chaii elseif hudaina elif hunxa 
    print(f"{var3} is greater than {var2}")             #yaha maile suru ma f lekheko xu kinaki hamle c ma code garda %d garnu parthyo testaii yesma format milauna
else:
    print(f"{var3} is less than {var2}")                #python ma chaii indentation error aaunxa matlab yesma harek code haru laii form ma lekhnu parney hunxa that means print ko aagadi tab space xa nii testaii tyo sab check garnu parxa if maile without tab space print func lekhthiye bhani tyo error aaunthyo


"""
for example maile indentation ko laagi
print("{var3} is less than {var2}")    ----> yesma print bhanda aagadi tab space theana so indentation error show garxa 
        yesto loops soops haru ko laagi
"""

# #list check

# list1 = [2,3,4,5,6,7,1,8,9,10]

# print("\n", 5 in list1)                                 #Boolean ma output dinxa true or false rw yo line ma chaii aahile -> True aaunxa

# if 5 in list1:
#     print("\nYes it is present in list")
# else:
#     print("\nNo it's not present in list")


#User Input List Check

list2 = [2,4,5,6,7,8,9]
key = int(input("\nEnter any number to check in list: "))

print(key not in list2)                                     #yesma chai list ma xaina bhaneko xa so boolean output --> True or False aaunxa if value maile 15 rakhey bhaney true aaunxa

if key in list2:
    print(f"{key} is present in list")
else:
    print(f"{key} is not present in list")



#Driving License Qualification Test

age = int(input("\nEnter your age: "))

if age<10 or age>100:
    print("Invalid age.")
elif age == 18:
    print("We will think about you.")
elif age>18:
    print("You can drive.")
else:
    print("You can't drive.")
