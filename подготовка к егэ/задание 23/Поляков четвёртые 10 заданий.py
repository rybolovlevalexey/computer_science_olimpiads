dp = [0] * 36
dp[20] = 1
for i in range(21, 36):
    dp[i] = dp[i - 2] + dp[i - 3] + dp[i - 5]
print(dp)
