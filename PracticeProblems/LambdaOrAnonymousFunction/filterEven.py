# Filter Even Numbers
"""
From List
Use filter() + lambda
"""

List = [1,3,2,5,6,4,7,2]

EvenFilter = list(filter(lambda x: x % 2 == 0, List))

print("The even numbers from the given List are", EvenFilter)