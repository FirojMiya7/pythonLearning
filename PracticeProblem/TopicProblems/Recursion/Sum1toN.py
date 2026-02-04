# Sum 1 to N using Recursion


def sum(n):
    if n <= 0:                          # yaha yo (base case (compulsory)) if kina rakheko cuz recursion infinite way ma call gareko garai garxa so 0 ma pugney bittikai cancel garna ko laagi compulsory nai ho yo 
        return 0
    return n + sum(n-1)

n = int(input("Enter any number: "))

print(f"The sum of 1 to {n} is", sum(n))