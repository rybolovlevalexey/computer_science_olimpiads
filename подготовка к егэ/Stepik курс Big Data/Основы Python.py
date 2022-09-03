n, m = map(int, input().split())
cnt = 0
sp = list()
for i in range(n):
    st = list(map(int, input().split()))
    sp.append(st)
for elem in sp:
    num = min(elem)
    for i in range(len(elem)):
        if num == elem[i]:
            flag = True
            for j in range(n):
                if sp[j][i] > num:
                    flag = False
                    break
            if flag:
                cnt += 1
print(cnt)