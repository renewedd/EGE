l = []
from re import *
with open("24_6054.txt") as f:
    data = f.readline()
# pattern = r"([BC][BC][A])*"
pattern = r"([^A]{2}[A])*"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))
