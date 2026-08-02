with open("2401.txt") as f:
    data = f.readline()
data = data.replace("ad", "a d")
data = data.replace("da", "d a")
data = data.split(" ")

answer = max(data, key=len)
print(len(answer))