from re import *
with open("24_4627.txt") as f:
    data = f.readline()
l = []

pattern = "(NPO|PNO)*"
m = finditer(pattern, data)
for i in m:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 3)


