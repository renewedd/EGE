from re import *
with open("24_2425.txt") as f:
    data = f.readline()
pattern = r"(DBAC)*((DBA)|(DB)|(D))"
l = [i.group() for i in finditer(pattern, data)]

answer = max(l, key=len)
print(len(answer))