# Tower of Hanoi


def TOH(n , a, b, c):
    if n > 0:
        TOH(n-1, a, c, b)
        print(f"Move disk:", n,"from", a,"to", b)
        TOH(n-1, c, b, a)

n = 3

TOH(n, 'a', 'b', 'c')

