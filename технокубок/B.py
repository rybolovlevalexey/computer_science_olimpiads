t = int(input())
for i in range(t):
    n = int(input())
    tup = tuple(map(int, input().split()))
    all_tup = set()
    all_tup.add(tup)
    k = 0
    flag = False
    while True:
        x = tup[-1]
        tup = tuple(j for j in tup if j <= x) + tuple(j for j in tup if j > x)
        if tup in all_tup and not flag:
            flag = True
        if tup in all_tup and flag:
            break
        k += 1
        all_tup.add(tup)
    print(k)
