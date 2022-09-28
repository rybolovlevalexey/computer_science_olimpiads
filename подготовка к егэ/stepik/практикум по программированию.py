st = input().split()
ans = list()
ans.append([])
for d in range(len(st) + 1):
    for s in range(len(st)):
        if s + d >= len(st):
            break
        subset = st[s:s+d+1]
        ans.append(subset)
print(ans)