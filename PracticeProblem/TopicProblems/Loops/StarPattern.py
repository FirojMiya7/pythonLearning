# Star Pattern

rows = 7

# First
"""
    *
    *
    *
    *
    *
    *
    *
"""

for i in range(rows):
    print("*")


# Second
"""
    *
    **
    ***
    ****
    *****
    ******
    *******
"""

for i in range(rows):
    print("*" * i)


# Third
"""
         *
        **
       ***
      ****
     *****
    ******
"""

for i in range(rows):
    print(" " * (rows-i-1), "*" * i)


# Fourth
"""
         *
        ***
       *****
      *******
     *********
    ***********
"""

for i in range(rows):
    print(" " * (rows-i-1), "*" * (2 * i - 1))


# Fifth
"""
    *******
    ******
    *****
    ****
    ***
    **
    *
"""

for i in range(rows, 0, -1):
    print("*" * i)