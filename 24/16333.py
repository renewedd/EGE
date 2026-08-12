with open("24_16333.txt") as f:
    data = f.readline()
data = data.replace("Q", "a")
data = data.replace("W", "a")
data = data.replace("R", "a")

data = data.replace("1", "0")
data = data.replace("2", "0")
data = data.replace("4", "0")
while "aa" in data or "00" in data:
    data = data.replace("aa", "a a")
    data = data.replace("00", "0 0")

data = data.split(" ")
answer = max(data, key=len)
print(len(answer))

