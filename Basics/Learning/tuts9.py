"""Grocery item ma jastaii
"""

grocery = ["Harpic", "Vim bar", "deodrant", "Bhindi", "Lollipop",56]

print(grocery)              #whole grocery nai print garxa
print(grocery[3])           #Index number 3 ko value print hunxa --> Bhindi

#Slicing 
print(grocery[0:4])         #Index number 0 dekhi 3 samma ko print garxa cus 4 excluded hunxa or n-1 ma kaam garxa
print(grocery[2:5])         #Index number 2 dekhi 4 ko samma ko linxa ani dekhaunxa

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

#Max and Min Number Print
print(max(numbers))
print(min(numbers))


#Append or kunai extra elemnt in the str array 
numbers.append(6)
numbers.append(65)
numbers.append(56)
print(numbers)

#Replace garna ko laagi Insert() func
numbers.insert(1,5)         #insert func le chaii euta index ma bhako data or value laii given data le replace garxa where (1,5) means where 1 --> index which neeed to be replaced and second 5 is value jun aaba gayera teii index number ma gayera basxa:
print(numbers)

#Remove garna ko laagi Remove() function
numbers.remove(2)           #Yesko bhitra feri direct value j laii hataune ho tesailaii nai mention garinxa aaru ko jasto index haina
print(numbers)

#Pop funtion le k garxa
numbers.pop()               #yesle chaii last index ma bhako value laii remove gardinxa
print(numbers)

"""
Mutable = Can Change / Changeable

Immutable = can not change ?non-changeable
"""



tp = (1,2,3)                #small bracket ma with coma value deko bhayera values laii yo aaba tupple bhayo and if coma nadeko bhaye tupple huntheana lah
print(tp)

#print(tp([1]))              #index 1 ko print hudaina  cuz tupple immutable hunxa so change hudaina error show garxa..


#Swapping
a=1
b=4
a,b = b,a
print("a = ", a, "b = ", b)

