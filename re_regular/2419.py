from re import *
with open("24_2419.txt") as f:
    data = f.readline()
pattern = r"C*"

l = [i.group() for i in finditer(pattern, data)]

answer = max(l, key=len)
print(len(answer))