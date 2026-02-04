# Square List
"""
List
Use map() + lambda
"""

List = [1,3,2,5,6,4,7]

square = list(map(lambda x: x*x , List))

print("Square of each elements of given List is:", square)