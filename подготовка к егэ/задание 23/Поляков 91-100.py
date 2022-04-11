dp = [0] * 23
dp[22] = 1
for i in range(21, 1, -1):
    i1 = 4 * i // 3
    if i + 3 <= 22:
        res = dp[i + 1] + dp[i + 3]
    else:
        res = dp[i + 1]
    if 0 <= i1 <= 22:
        res += dp[i1]
    dp[i] = res
print(dp)
