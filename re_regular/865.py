from re import *
with open("24_865.txt") as f:
    data = f.readline()
pattern = r"[^CF]*"
l = [i.group() for i in finditer(pattern,data)]

answer = max(l, key=len)
print(len(answer))
