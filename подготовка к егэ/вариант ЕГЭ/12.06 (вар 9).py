file = open('28133_B.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
ans = 0
anssp = list()
for i in range(n - 1):
    for j in range(i + 1, n):
        if sp[i] > sp[j] and (sp[i] + sp[j]) % 120 == 0 and sp[i] + sp[j] > ans:
            ans = sp[i] + sp[j]
            anssp = [sp[i], sp[j]]
print(anssp)