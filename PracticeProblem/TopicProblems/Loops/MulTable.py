# Multiplication Table
# Print table of a number

# range(start, stop, step) --------- For eg. range(1, 11, 2) ----------- Output --> 13579



def MulTable(n, limit):
    for i in range(1, limit + 1):                   #range(start, stop, step)

        print(f"{n} x {i} =", n * i)

try:
    n = int(input("\nEnter number: "))
    limit = int(input("Enter limit: "))

    print(f"\nMultiplication Table of {n}:")
    MulTable(n, limit)

except ValueError:
    print("Error! Enter Integer only.")


    