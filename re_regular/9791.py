#123456789ABCDEF
l = []
from re import *
with open("24_9791.txt") as f:
    data = f.readline()
pattern = r"[123456789ABCDEF]*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))


