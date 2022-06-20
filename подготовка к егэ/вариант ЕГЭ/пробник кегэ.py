ans = list()
for a in range(10000):
    flag = True
    for x in range(10000):
        res = (x & a == 0) or (x & 17 != 0) or (x & 5 != 0) or (x & 3 != 0)
        if not res:
            flag = False
            break
    if flag:
        ans.append(a)
print(ans)
print(max(ans))