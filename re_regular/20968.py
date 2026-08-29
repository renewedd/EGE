l = []
from re import *
with open("24_20968.txt") as f:
    data = f.readline()
num = r"(([1-9][0-9]*[02468])|[02468])"
pattern = rf"(({num}[*+])*{num})"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))