dp = [0] * 31
dp[21] = 1
for i in range(22, 31):
    dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 6]
print(dp)
