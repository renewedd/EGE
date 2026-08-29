from re import *
l = []
with open("24_23381.txt") as f:
    data = f.readline()
pattern = r"[02468][A-Z]*[02468]"
f = finditer(pattern, data)
for i in f:
    m = i.group()
    s = set(m[1:-1])
    if len(s) == 1:
        l.append(i.group())
answer = max(l, key=len)
print(len(answer))
