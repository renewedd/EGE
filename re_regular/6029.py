from re import *
l = []
with open("24_6029.txt") as f:
    data = f.readline()

pattern = r"((EF)*E?)|((FE)*F?)"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))