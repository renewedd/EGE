l = []
from re import *
with open("24_3228.txt") as f:
    data = f.readline()

pattern = r"(AB|AC)*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 2)