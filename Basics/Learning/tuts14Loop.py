#Loops in Python

#For Loop

#in case of list
"""list1=["Feroz","Siroj","Sushil","Samyam"]
for item in list1:
    print(item)                 #list1 ma bhako sabaii print gardinxa."""


#incase of tupple
"""list2=("Feroz","Siroj","Sushil","Samyam","Trishan")
for item in list2:
    print(item)"""


#in list Feroz le kati chocolate khanxa wala case ma
"""list3=[["Feroz",3], ["Sushil", 4], ["Trishan",6],["Samyam",1]]
for item in list3:
    print(item)                     #['Feroz', 3] yesari sabai print garxa...

for item, chocolate in list3:
    print(item)                     #Feroz  Sushil bhandai main main key or item matra print garxa.

for item, chocolate in list3:
    print(item, "eat", chocolate ,"chocolates")                 #Feroz eat 3 chocolates yesari print garxa output"""


#aaba dictionary ma 
"""list3=[["Feroz",3], ["Sushil", 4], ["Trishan",6],["Samyam",1]]

dict1=dict(list3)
print(dict1)                            #{'Feroz': 3, 'Sushil': 4, 'Trishan': 6, 'Samyam': 1} dictionary print garxa.

# for item, chocolate in list3:
#     print(item, "eat", chocolate ,"chocolates")

for item, chocolate in dict1.items():               #dictionary le aarko list ko data lai inherit gareko xa tei bhayera bhitra ko item lai use garna ko laagi items() use gareko ho
    print(item, "eat", chocolate ,"chocolates")

for item in dict1:
    print(item)                                         #main key haru print garxa without items()"""


# Quiz
#List->print number which is greater than 6
"""
items=["Feroz",34,45,"354",2,3,455,6,67,"7"]

# for item in list:
#     if type(item)==int:                            #yesari chai output error aaunxa haala ki program right naii xa..
#         if(item>=6):
#             print(item)
#         else:
#             print("There is no number greater than 6")

#Instead we do

for item in items:
    if str(item).isnumeric() and int(item) > 6:                 #item lai str ma convert garxa  ani numeric value ho ki nai check garxa if ho bhani again int ma convert garera compare garxa ani print output
        print(item)
"""




#While Loop

"""
i=0
while(i<15):
    print(i)                #infinite loop ma print o gari rakhxa until i use i=i+1;
    i=i+1                   #o-14 samma print hunxa."""



#While loop kati bela use garney tw?
"""Kati choti loop chalxa thaha xaina
Condition based kaam xa
User input, file read, game loop jasto case"""

#For loop kati bela use garney tw?
"""List, tuple, string ma iterate garna
Fixed range xa
Counter use garna"""
