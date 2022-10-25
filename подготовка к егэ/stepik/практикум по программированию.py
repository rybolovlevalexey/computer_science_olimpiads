n = int(input())
ans = list()
for i in range(n):
    k = int(input())
    sp = list()
    for j in range(k):
        sp.append(input().split()[1] == '5')
    ans.append(any(sp))
print('YES' if all(ans) else 'NO')
