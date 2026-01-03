#Dictionary is nothing but key value pairs

L1 = []                 #Yo bracket le determine garxa so yo ho list
T2 = ()                 #Yo bracket le determine garxa so yo ho tupple

d1 = {}                 #Yo bracket le determine garxa so yo ho dictionary
print(type(d1))         #<class 'dict'> yesari output aaunxa dictionary ho dekhaunxa.


d2 = {"Feroz":"Pizza", "Sushil":"Burger",
      "Samyam":"Croissant",
      "Trishan":"Dhedo",
      "Suhan":{"B":"Roti",                      #where B=Breakfast , L=lunch, D=Dinner.
               "L":"Bhaat",
               "D":"Chicken"}}

#Self update or Addition and deletion in dictionary
d2["Aarambha"] = "Cup-Cake"
d2[340] = "Junk Food"


print(d2["Feroz"])
print("Feroz eat:", d2["Feroz"])
print("\n",d2)
#print(d2["Sushil","Feroz"])         #yedi duita ko chaiyo bhani yesari wrong hunxa error show garxa baru instead aarko use gara method.

#Multiple from dictionary
print("\nFeroz eat:", d2["Feroz"],
      "\nSushil eat:", d2["Sushil"],
      "\nSamyam eat:", d2["Samyam"], 
      "\nTrishan eat:",d2["Trishan"])

#Dictionary ko Dictionary
print("\n",d2["Suhan"])                #whole dictionary of suhan naii print gardinxa aahile laii..
print("\nSuhan ko breakfast:",d2["Suhan"]["B"],             #yesma pani xutta xuttai naii print garna parxa
      "\nSuhan ko Lunch:",d2["Suhan"]["L"])     

#self update wala ko laagi addition deletion ko example
print(d2)                              #Aarambha ko pani name include bhayera aayo ani 340 ko pani aayo but

# aaba chaii tyo hero banyo 340 wala dictinary solti aaba teslai chaii delete garddey mah tero output ma dekhina chahanna bhanyo now,

del d2[340]                              #yesley delete gardiyo yo dictinary lai dictinary ma tw xa but output ma show hudaina after this command or upcoming lines
print(d2)
