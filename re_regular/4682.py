from re import *
l = []
with open("24_4682.txt") as f:
    data = f.readline()
pattern = r"([AE][BCD])*"
for i in finditer(pattern, data):
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 2)


