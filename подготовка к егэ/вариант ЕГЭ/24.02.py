file = open('17.txt', 'r')
sp = file.read().strip().split('\n')
sp = list(map(int, sp))
sr = sum(filter(lambda x: x % 2 == 0, sp)) / len(list(filter(lambda x: x % 2 == 0, sp)))
cnt = 0
ans = -1
for i in range(len(sp) - 1):
    if (sp[i] % 3 == 0 or sp[i + 1] % 3 == 0) and (sp[i] < sr or sp[i + 1] < sr):
        cnt += 1
        if sp[i] + sp[i + 1] > ans:
            ans = sp[i] + sp[i + 1]
print(cnt, ans)