n = int(input())
i = 1
num = 1
sp = list()
while len(sp) < n:
    r = list()
    for j in range(num, num + i):
        r.append(j)
    print(r)
    num += i
    i += 1
    r = r[::-1]
    sp.extend(r)
ans = list()
i = 0
while len(ans) < n:
    ans.append(sp[i])
    i += 1
print(*ans)
