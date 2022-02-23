file = open('Zadanie_27-B.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
sp = list(sorted(map(int, sp)))
ans_sum = -1
ans = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (sp[i] + sp[j]) % 1011 == 40 and (ans_sum == -1 or ans_sum > (sp[i] + sp[j])) and sp[i] > sp[j]:
            ans_sum = (sp[i] + sp[j])
            ans = [sp[i], sp[j]]

print(ans_sum)
print(ans)