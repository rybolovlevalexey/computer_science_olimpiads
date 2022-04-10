dp = [0] * 23
dp[22] = 1
for i in range(21, 1, -1):
    i1 = 3 * i + 1
    i2 = 3 * i + 2
    i3 = 3 * i
    if i + 3 <= 22:
        res = dp[i + 1] + dp[i + 3]
    else:
        res = dp[i + 1]
    if 0 <= i1 <= 22:
        res += dp[i1]
    if 0 <= i2 <= 22:
        res += dp[i2]
    if 0 <= i3 <= 22:
        res += dp[i3]
    dp[i] = res
print(dp)
