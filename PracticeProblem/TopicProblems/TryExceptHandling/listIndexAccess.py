# List Index Access using try except handling also function.
"""
Input: list + index
Handle IndexError
"""


def IndexAccess():
    size = int(input("Enter the size of list: "))
    List = []

    for i in range (0,size):                # excluded hunxa means size = size - 1 (5 size diye pani 4 samma hunxa 0 to 4)
        List.append(input("Enter any value: "))

    index = int(input("Enter index you want to access from List: "))

    try:
        print("There is", List[index] , f"in index {index}")

    except IndexError:
        print("Error! List index out of range.")


IndexAccess()