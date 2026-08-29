with open("24_26551.txt") as f:
    data = f.readline()
l = []
from re import *
with open("24_9845.txt") as f:
data = f.readline()
pattern = r"*|&*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))