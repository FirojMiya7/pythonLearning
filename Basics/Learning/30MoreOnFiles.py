# Reading file pointer position using tell()
"""
f = open("Basics/Learning/Feroz.txt","r")

print(f.tell())                 # At the beginning, pointer is at position 0 where tell() returns 0
print(f.readline())

print(f.tell())                 # tell le file pointer ko current position ma return garcha
print(f.readline())

print(f.seek(25))               # seek le file pointer lai specified position ma move garcha matlab 25th position baata read garna thalcha
print(f.readline())

f.close()
"""