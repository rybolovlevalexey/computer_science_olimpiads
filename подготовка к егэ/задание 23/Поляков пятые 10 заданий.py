dp = [0] * 11
dp[3] = 1
for i in range(4, 11):
    if (i + 1) % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[(i + 1) // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)