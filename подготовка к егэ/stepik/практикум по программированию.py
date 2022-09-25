import itertools
k, n = map(int, input().split())
sp = list(i for i in range(0, n))
res = itertools.permutations(sp, k)
ans = list()
for elem in res:
    if sorted(elem) not in ans:
        ans.append(sorted(elem))
for elem in ans:
    print(*elem)