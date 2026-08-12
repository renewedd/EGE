with open("2411.txt") as f:
    data = f.readline()
data = data.replace("12", "1 2")
data = data.replace("21", "2 1")
data = data.replace("13", "1 3")
data = data.replace("31", "3 1")

data = data.split(" ")
answer = max(data, key=len)
print(len(answer))