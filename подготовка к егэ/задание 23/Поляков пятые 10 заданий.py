dp = [0] * 12
dp[2] = 1
for i in range(3, 12):
    if (i + 1) % 2 == 0:
        dp[i] = dp[i - 2] + dp[i - 3] + dp[(i + 1) // 2]
    else:
        dp[i] = dp[i - 2] + dp[i - 3]
print(dp)
