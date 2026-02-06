#Tower of Hanoi

def TOH(n, a, b, c):            #TOH --> Tower Of Hanoi
    if n > 0:
        TOH(n-1, a, c, b)
        print("Move disk", n,"from", a,"to", b)
        TOH(n-1, c, b, a)

n = int(input("Enter number of hanois: "))

TOH(n,'a','b','c')