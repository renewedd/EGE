with open("2417.txt") as f:
    data = f.readline()
data = data.replace("Q", "*")
data = data.replace("R", "*")
data = data.replace("S", "*")

data = data.replace("**", "* *")
data = data.split(" ")

answer = max(data, key=len)
print(len(answer))


