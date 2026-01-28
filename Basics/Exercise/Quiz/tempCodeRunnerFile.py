
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a                     # yield le generator function banauxa yo return jasto ho tara yo function ko state lai pani save garcha
        a, b = b, a + b
number = int(input("Enter Limit: "))
print("Fibonacci Series: ", list(fibonacci(number)))    # list() le generator function ko sabai values lai list ma convert garcha and print garcha
