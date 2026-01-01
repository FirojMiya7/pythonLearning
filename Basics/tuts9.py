"""Grocery item ma jastaii
"""

grocery = ["Harpic", "Vim bar", "deodrant", "Bhindi", "Lollipop",56]

print(grocery)              #whole grocery nai print garxa
print(grocery[3])           #Index number 3 ko value print hunxa --> Bhindi
print(grocery[0:4])         #Index number 0 dekhi 3 samma ko print garxa cus 4 excluded hunxa or n-1 ma kaam garxa
#print(grocery[6])          #Index number 6 is not present so error occurs


#Sorting functions haru ko laagi heram haii tw

numbers = [2,4,9,11,3,7]

print(numbers)              #originally numbers ma j j xa exact copy show garxa
 

#Sorted Function
numbers.sort()              #SORTING Function ho
print(numbers)              #yaha chaii line 18 ma sort hunxa ani 19 ma print hunxa teii sorted values


#Sorted Reverse Function
numbers.sort()
numbers.reverse()           #REVERSE garney Function ho
print(numbers)              #line 21 le gareko sort func le sort garxa ani teii sorted value laii reverse funtion le chaii reverse garera ultari print gari dekhaunxa

