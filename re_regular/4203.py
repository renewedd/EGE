l = []
from re import *
with open("24_4203.txt") as f:
    data = f.readline()

pattern = r"(AB|CB)*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 2)
