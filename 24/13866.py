with open("24_13866.txt") as f:
    data = f.readline()
data = data.replace("1","*")
data = data.replace("3","*")
data = data.replace("5","*")
data = data.replace("7","*")
data = data.replace("9","*")
l = 0
m = 0
for right in range(len(data)):
    l += 1
    if data[right] == "*" and data[right + 1] == "*" and data[right + 2] == "*":
        l = 2
    m = max(m, l)
print(m)
