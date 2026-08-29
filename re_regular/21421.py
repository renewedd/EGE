
l = []
from re import *
with open("24_21421.txt") as f:
    data = f.readline()
pattern = r"[123456789AB][0123456789AB]*[02468A]"
#0123456789AB
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))
