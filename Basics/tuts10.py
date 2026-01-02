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

print(d2["Feroz"])
print("Feroz eat:", d2["Feroz"])
print("\n",d2)
#print(d2["Sushil","Feroz"])         #yedi duita ko chaiyo bhani yesari wrong hunxa error show garxa baru instead aarko use gara method.

#Multiple from dictionary
print("\nFeroz eat:", d2["Feroz"],"\nSushil eat:", d2["Sushil"],"\nSamyam eat:", d2["Samyam"], "\nTrishan eat:",d2["Trishan"])