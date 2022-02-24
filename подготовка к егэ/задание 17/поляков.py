ans = []
for x in range(1606, 9680 + 1):
    if x % 11 == 0 and x % 7 != 0 and x % 13 != 0 and x % 17 != 0 and x % 19 != 0:
        ans.append(x)
print(len(ans), max(ans))
