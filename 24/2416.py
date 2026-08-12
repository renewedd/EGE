with open ("2416.txt") as f:
    data = f.readline()

data = data.replace("B", "*")
data = data.replace("C", "*")
data = data.replace("D", "*")

data = data.replace("A", "1")
data = data.replace("E", "1")

data = data.replace("1*", "0")

