ans = []
for n in range(1, 5000):
    r = bin(n)[2:]
    r = r + str(r.count("1") % 2)
    r = r + str(r.count("1") % 2)
    r = int(r, 2)
    if r > 77:
        ans.append(n)
print(min(ans))
