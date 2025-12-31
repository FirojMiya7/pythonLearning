mystr = "Ferozali is a good boy"       #hamilaii thaha nai xa ki yo sab character haru index ma kaam garxa
#maile yettikai run garey bhani k e pani output aaudaina  but after adding print 

print(mystr)            #mystr print bhayo
print(mystr[11])        #to print just g from the characters of mystr---> given index number where g stored
print(mystr[0:5])       #To print whole word Feroz from the mystr---> where index 0 is included and index 5 is excluded
print(len(mystr))       #To find out the total number of index in a given mystr.. 19 bhanera dinxa 
#incase maile 
print(mystr[0:100])     #Yesari print garey bhani index 19 samma bhako print gardinxa baaki extra index laii chaii error bhanera show gardaina
print(mystr[0:5:2])     #yesma chaii 0 dekhi 5 index samma ko character ma euta euta skip gardai print garxa Feroz-->F r z where [0:5:2] 0-initial index, 5-destinationIndex, 2reduction index where n-1 is applied if 2 lekhiyeko xa bhani 2-1>1 skip 3-1>2 skip
#incase [:]-->suru ko ma 0 initial aafai linxa, second ko ma all index linxa automatic again inCase[::]-->suru ko ma 0 initial aafai linxa, second ko ma all index linxa automatic,and in the last reduction wala ma chai be Default 1 hunxa so yesley aafai 1 linxa.
print(mystr[::])        #Act neutral