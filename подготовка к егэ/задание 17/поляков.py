ans = list()
for x in range(2595, 8401 + 1):
    if x % 2 == 0 and x % 13 != 0:
        ans.append(x)
print(len(ans), sum(ans))