#Break and Continue in loop


"""i=0
while(i<10):
    print(i, end=" ")               #end=" " space diney or \t ko jasto kaam garxa --> output-> 0 1 2 3 4 5 6 7 8 9 
    i=i+1"""

# Break and continue

"""i=0
while(True):                                #only True use garera print garney ho bhane infinite hunxa
    print(i+1, end=" ")

    if(i==4):
        i=i+1
        continue

    if(i==9):
        break                       # stop the loop   yaha aayera if i==9 then break and exit 
    i = i+1"""


#Quiz
#Write a program to take input from user till the input number is greater than 50
"""
while(True):
    inp=int(input("\nEnter a number: "))
    if inp>50:
        print("\nCongrats you have entered a number greater than 50")
        break
    else:
        print("\nTry again! Its smaller than 50")
        continue"""
