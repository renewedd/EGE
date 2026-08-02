with open("2410.txt") as f:
    data = f.readline()
data = data.replace("00", "0 0")
data = data.split(" ")

answer = max(data, key = len)
print(len(answer))