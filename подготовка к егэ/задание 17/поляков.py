ans = list()
for x in range(10, 1178 + 1):
    if x % 2 == 0 and x % 10 != 0 and x % 10 != 2 and x % 10 != 6 and x % 10 != 8 and x % 100 != 14:
        ans.append(x)
print(sum(ans), min(ans))