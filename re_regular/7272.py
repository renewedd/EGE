from re import *
with open ("24_7272.txt") as f:
    data = f.readline()

pattern = r"(AB|CB)*"
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer)/2)