file = open('17.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
sr = sum(sp) / len(sp)
cnt = 0
ans = -1
for i in range(len(sp) - 1):
    if (sp[i] % 5 == 0 or sp[i + 1] % 5 == 0) and (sp[i] < sr or sp[i + 1] < sr):
        cnt += 1
        if sp[i] + sp[i + 1] > ans:
            ans = sp[i] + sp[i + 1]
print(cnt, ans)
