file = open('273361.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mn = None
for i in range(len(sp) - 1):
    if (sp[i] + sp[i + 1]) % 5 == 0:
        cnt += 1
        if mn is None or mn > (sp[i] + sp[i + 1]):
            mn = (sp[i] + sp[i + 1])
print(cnt, mn)