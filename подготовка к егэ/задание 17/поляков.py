ans = []
for x in range(3201, 12876 + 1):
    if x % 4 == 0 and x % 11 != 0 and x % 13 != 0 and x % 7 != 0 and x % 19 != 0:
        ans.append(x)
print(len(ans), max(ans))
