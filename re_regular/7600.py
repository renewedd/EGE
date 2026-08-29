from re import *
l = []
with open("24_7600.txt") as f:
    data = f.readline()
pattern = r"([^QRS]*[QRS][^QRS]+)*[QRS]?"
#QAAAR
#AAAAQAAAR
#QAAARAAAA
#QAAAASMMRII
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))