from re import *
with open("24_3792.txt") as f:
    data = f.readline()
pattern = r"[ABC]*"
l = [i.group() for i in finditer(pattern, data)]

answer = max(l, key=len)
print(len(answer))