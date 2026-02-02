# Lambda or Anonymous Functions in Python

#Regular function definition
"""
def add(x, y):
    return x + y

print("Regular Function:", add(5, 3))
"""


#Lambda function definition
"""
add = lambda x, y: x + y                # Similar to regular function but more concise(explain something in a short clear way)  (single expression)

print("Lambda Function:", add(5, 3))
"""





#Example with filter() and lambda
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))            # filter le chaii list ko sabai element haru ma lambda function apply garxa ani true value return garne element haru matra nikalxa    
print("Even Numbers using Lambda and filter():\n", even_numbers)
"""


#Example with map() and lambda
"""
squared_numbers = list(map(lambda x: x ** 2, numbers))              # map le chaii list ko sabai element ma lambda function apply garxa and loop ko iteration jasto kaam garxa
print("Squared Numbers using Lambda and map():\n", squared_numbers)
"""


#Example with sort() and lambda
"""
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
points.sort(key=lambda point: point[1])                     # sort garne bela ma key vanne parameter use garera lambda function define garxa ani y-coordinate anusar sort garxa
print("Points sorted by y-coordinate using Lambda and sort():\n", points)
"""


#Example with reduce() and lambda
"""
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)               # reduce le chaii list ko sabai element haru ma lambda function apply garxa ani ek single value return garxa (jasto ki product) 
print("Product of all numbers using Lambda and reduce():\n", product)
"""
