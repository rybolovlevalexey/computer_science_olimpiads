dp = [0] * 16
dp[1] = 1
for i in range(2, 16):
    dp[i] = dp[i - 1]
    if i % 10 == 0:
        dp[i] += dp[i // 10]
    if i % 2 == 0:
        dp[i] += dp[i // 2]
    else:
        dp[i] += dp[(i - 1) // 2]
print(dp)
print(dp[-1])
