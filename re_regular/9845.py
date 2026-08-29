l = []
from re import *
with open("24_9845.txt") as f:
    data = f.readline()
#   (A8)(B9)(C9)
#   (A8)(B9)(C9)   B
#8  (A9)(B9)  C
#8  (A9)(B9)(C9)
pattern = r"[89]?([ABC][89])*[ABC]?"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))