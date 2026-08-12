with open("24_1873 (2).txt") as f:
    data = f.readline()
data = data.replace("P", "*")
data = data.replace("R", "*")
while "**" in data:
    data = data.replace("**", "* *")
    # data = data.replace("PR", "P R")
    # data = data.replace("RP", "R P")
data = data.split(" ")
answer = max(data, key=len)
print(len(answer))