# 1873
with open("24_1873.txt") as f:
    data = f.readline()
data = data.replace("P", "*")
data = data.replace("R", "*")
data = data.replace("**", "* *")
data = data.split(" ")
answer = max(data, key=len)
print(len(answer))

# 16333
with open("24_13866") as f:
    data = f.readline()
data = data.replace("1","*")
data = data.replace("3","*")
data = data.replace("5","*")
data = data.replace("7","*")
data = data.replace("9","*")
data = data.replace("***", "* * *")
data = data.split(" ")
answer = max(data, key=len)
print(len(answer))



# 13866
with open("24_1873") as f:
    data = f.readline()
data = data.replace("1","*")
data = data.replace("3","*")
data = data.replace("5","*")
data = data.replace("7","*")
data = data.replace("9","*")
data = data.replace("***", "* * *")
data = data.split(" ")
answer = max(data, key=len)
print(len(answer))

# 2411

# задачи с номером на 24 - с futurestep
# остальные с кэге
#https://kompege.ru/task
#https://future-step.ru/task/?task_search=+2417
