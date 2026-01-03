#SET like in mathematics

s = set()
# print(type(s))                                    #yo set ho bhanera output aaunxa


# s_from_list = set([1,2,3,4])
# l = [3,4,5,6]
# s_from_list_anotherMethod = set(l)                #yo pani same ho but another method

# print(s_from_list)                                #output: [1,2,3,4] garxa.
# print(s_from_list_anotherMethod)                            #output: [1,2,3,4] garxa.
# print(type(s_from_list))                          #set ho bhanera print garxa

#aaba s = set() element add garna paryo ni tw

s.add(1)
# s.add(1)                                          #yo line useless xa kinaki set le same value jati ota bhaye pani euta matra element show garxa
s.add(2)
s.add(3)                                            #add element -> 3
s.remove(2)                                         #remove element -> 2

s1 = s.union({0,1,2,3,4})                           #duita set ko union as a whole 0,1,2,3,4 xa so sabai print hunxa.

s2 = s.intersection({1,2,3})                        #duita set ko intersection 1,2 hunxa so 1,2 print hunxa
print(s,s1,s2)

print(type(s1))                                     #yesle type -> set output dinxa
print(len(s1))                                      #yesle length of s1 -> 5 output dinxa
print(min(s1))                                      #yesle set ma bhako minimum element or smallest value dinxa-> 0 output
print(max(s1))                                      #yesle maximum or biggest element value -> 4 output dinxa