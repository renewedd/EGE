from re import *
l = []
with open("24_23206.txt") as f:
    data = f.readline()
pattern = r"[02468][^S02468]*([S][^S02468]*){35}"
#8M517 S195 S77W111 S
#4 7A SSHATSSS
f = finditer(pattern, data)
for i in f:
    l.append(i.group())
answer = max(l, key=len)
print(len(answer))