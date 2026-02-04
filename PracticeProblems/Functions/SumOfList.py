# Sum of List using function
"""
Input: list of integers
Output: sum of elements
"""


def sumOfList(List):
    total = 0
    for num in List:
        total += num
    return total
    
List = [2,3,6,7,4,2,4,46,1]

print(f"Total Sum of given list: {List} is",sumOfList(List))
