from re import *
with open("24_3584.txt") as f:
    data = f.readline()
l = []

pattern = "(BA|DA)*"
m = finditer(pattern, data)
for i in m:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 2)