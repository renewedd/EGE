
from re import *
l = []
with open("24_17685.txt") as f:
    data = f.readline()
num = r"(([1-9][0-9]*)|0)"
zero = rf"({num}\*)*0(\*{num})*"
pattern = rf"({zero}\+)*{zero}"
#5 * 5 * 0 + 10 * 0 * 5
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))
