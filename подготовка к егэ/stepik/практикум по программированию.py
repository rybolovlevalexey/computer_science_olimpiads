n = int(input())
if n == 1:
    print(input())
else:
    mx = None
    for i in range(n):
        flag = False
        st = list(map(int, input().split()))
        for j in range(n):
            if i == n - j - 1:
                flag = True
            if flag and (mx is None or mx < st[j]):
                mx = st[j]
    print(mx)