l = []
from re import *
with open("24_6636.txt") as f:
    data = f.readline()
pattern = r"([24][135])*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 2)

