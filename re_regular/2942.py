from re import *
with open("24_2942.txt") as f:
    data = f.readline()

pattern = r"(AB|AC)*"
s = finditer(pattern, data)
l = []
for i in s:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 2)
