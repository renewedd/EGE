l = []
from re import *
with open("24_6757.txt") as f:
    data = f.readline()
pattern = r"((CFE)|(FCE))*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 3)
