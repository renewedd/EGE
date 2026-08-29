l = []
from re import *
with open("24.23_19887.txt") as f:
    data = f.readline()
#(12)(34)(56)
#2 (12)(34)(56)
#2 (12)(34)(56) 5
#(12)(34)(56) 5
pattern = r"[02468]?([1359][02468])*[1359]?"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))
