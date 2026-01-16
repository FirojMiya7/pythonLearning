items=["Feroz",34,45,"354",2,3,455,6,67,"7",6.5]

found = False
for item in items:
    if type(item)==int or type(item)==float:                            #yesari chai output error aaunxa haala ki program right naii xa..
        if(item>=6):
            print(item)
            found = True

if not found:
    print("There is no number greater than 6")