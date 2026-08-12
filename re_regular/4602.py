from re import *
with open("24_4602.txt") as f:
    data = f.readline()
l = []

#pattern = r"(BA|CA|DA|BO|CO|DO)*"
pattern = r"([BCD][AO])*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer) / 2)

