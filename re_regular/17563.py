from re import *
l = []
#228 - 3 * 26
#05
#-50-10
# 1 10 19 123 120
with open("24_17563.txt") as f:
    data = f.readline()
num = r"[7-9][0789]*"
pattern = rf"({num}[-*])*{num}"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))

