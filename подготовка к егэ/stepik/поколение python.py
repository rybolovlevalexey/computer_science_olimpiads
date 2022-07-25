sp = list()
n = int(input())
for i in range(n):
    st = input()
    sp.append(list(map(int, list(st))))
dp = list()
for i in range(n):
    dp.append(list('*' * n))
dp[0][0] = sp[0][0]