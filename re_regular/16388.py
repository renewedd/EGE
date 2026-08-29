#MN KLMNKLM NK
#N KLMNKLMN KL
#KLMNKLMN KLM
#KLMNKLMN
from re import *
l = []
with open("24_16388.txt") as f:
    data = f.readline()
pattern = r"((LMN)|(MN)|(N))?(KLMN)*((KLM)|(KL)|(K))?"
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))