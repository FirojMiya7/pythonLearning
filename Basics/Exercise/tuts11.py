"""
Create a dictionary and take user input and return the meaning of the word from the dictionary

Literally euta dictionary joo banaune where i can search the meaning of word
"""

d1 = {"Mutable":"Changeable",
      "Immutable":"Unchangeable",
      "Nostalgia":"Longing for the past",
      "Diligent":"Hard working",
      "Hypothetical":"Imagined or Supposed",
      "Schedule":"Arrange or Plan"}

print("\nEnter the word to find meaning from the following words:")
print("Mutable \tImmutable \tNostalgia \tDiligent \tHypothetical \tSchedule \n")
inpWord = input("Enter the Word: ").capitalize()

print(f"The meaning of {inpWord} is {d1.get(inpWord,"not found in dictionary")}")
