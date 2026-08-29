l = []
from re import *
with open("24_31129.txt") as f:
    data = f.readline()
#(3 *) (2 -) (1 *) (2 -) 4
#-9 -5
num = r"(([1234][01234]*)|0)"
pattern = rf"({num}[*-])*{num}"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))