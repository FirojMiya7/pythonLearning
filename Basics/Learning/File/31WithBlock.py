# Block 

with open("Basics/Learning/File/Feroz.txt","r") as f:                    #with block le file automatically close garcha after the block ends

    a = f.readline() 
    b = f.read(7)

    print(a)    # First line read garera a ma store garyo ani print garyo
    print(b)    # Only 7 ota characters read garera b ma store garyo ani print garyo