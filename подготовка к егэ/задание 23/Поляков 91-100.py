dp = [0] * 23
dp[22] = 1
for i in range(21, 1, -1):
    if 0 <= i + 3 <= 22:
        dp[i] = dp[i + 3] + dp[i + 1]
    else:
        dp[i] = dp[i + 1]
print(dp)
res = dp[2]
for i in range(5, len(dp)):
    if i % 4 == 2:
        res += dp[i]
    elif i % 4 == 3:
        res += dp[i]
print(res)