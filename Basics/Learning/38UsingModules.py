# Using External or Inbuilt Modules in Python

# Module is a file containing Python code that can define functions, classes, and variables.
# It can also include runnable code. Modules help in organizing code and reusing it across different programs.



# Example 1: Using random module to generate random numbers

import random
randomNumber = random.randint(1, 100)           # Generates a random integer between 1 and 100 including 1 and 100 both.
print("Random Number between 1 and 100 is:", randomNumber)



rand = random.random()                          # Generates a random float number between ( 0.0 to 1.0 default)
print("Random float number between 0.0 to 1.0 is:", rand)


rangeRandom = random.uniform(1, 5)              # Generates a random float number between ( 1.0 to 5.0 ) custom range.
print("Random float number between 1.0 to 5.0 is:", rangeRandom)