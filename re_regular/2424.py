from re import *
with open("24_2424.txt") as f:
    data = f.read()

pattern = r"(XYZ)*"
l = [i.group() for i in finditer(pattern, data)]
answer = max(l, key=len)
print(len(answer))