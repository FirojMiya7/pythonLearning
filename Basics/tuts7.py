#Variable

var1 = "Hello World"
var5 = "56"             #yo pani characeter string ho cuz duita double quote ko bhitra lekhiyeko xa ni tw
var6 = "24"
var2 = 4
var3 = 3.14
var4 = var2 + var3
var7 = var5 + var6
var8 = int(var5) + int(var6)

"""
variable data type switch garna ko laagi haami sanga 3 ota function hunxa like string ma xa bhani int ma ligney for example just like the above one
they are:
int()
float()
str()
"""

print(var1)
print(var2)
print(var3)

print("Sum is ", var4)
print("Sum is ", var7)              #value aauda output 56 rw 24 aayo cuz duitai yaha character ma thea so char addition bhayesi concatination hunxa
print("Sum is ", var8)

print(type(var1))
print(type(var2))
print(type(var3))



#To print single statements multiple times like loop 

print(10 * "Hello World\n")

print(10 * int(var5) + int(var6))           #10*56+24=>584

print(10 * str(int(var5) + int(var6)))          # yesma chaii var5 given str ho now yeslaii hamle suru ma int ma convert garxam ani int add hunxa 56 +24 and then tyo convert hunxa again str ma and then multiply with 100



#User INput 

print("Enter any two number: ") 
inpNum1 = input()               #suru mai input huney bela mai yo str ma input linxa so hamilaii paxi addition garna paryo bhani datatype convert garera int or float ma change garera garnu parney raixa
inpNum2 = input()
sum = int(inpNum1) + int(inpNum2)
print("The sum of your given numbers: ", sum)