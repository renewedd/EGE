l = []
from re import *
with open("24_31368.txt") as f:
    data = f.readline()
#2 * 3 * 0 + 91 * 120 * 0 + 91 * 120 * 0
#2 * 3 * 0
#0 * 2 * 3
#2 * 0 * 3
num = r"([1-9][0-9]*|0)"
zero = rf"({num}\*)*0(\*{num})*"
pattern = rf"({zero}\+)*{zero}"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))
