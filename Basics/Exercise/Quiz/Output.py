#Guess the Output:


items = ["Shirt", "Pants", "Socks", "Hat"]

for item in items:
    if item == "Socks":         # skips the iteration when item is "Socks"
        continue
    print(item)


for item in items:
    print(item[0], end=" ")    # prints the first letter of each item in the same line yaha end = " " ka matlab space diyera print garney otherwise next line ma print gathyo