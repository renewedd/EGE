from re import *
l = []
with open("24_22356.txt") as f:
    data = f.read()
pattern = r"[1-9AB][0-9AB]*[13579B]"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(data.find(answer))