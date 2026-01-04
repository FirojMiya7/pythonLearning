"""
If else , elif conditions
"""


var1 = 26
var2 = 54

var3 = int(input("Enter any Number:"))
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