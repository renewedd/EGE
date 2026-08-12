from re import *
l = []
with open("24_1975.txt") as f:
    data = f.readline()

pattern = r"[^P]*(P[^P]+)*P?"
f = finditer(pattern, data)
for i in f:

    l.append(i.group())
answer = max(l, key=len)
print(len(answer))



