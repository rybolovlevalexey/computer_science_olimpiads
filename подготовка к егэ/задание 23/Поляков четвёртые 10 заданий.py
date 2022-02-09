dp = [0] * 31
dp[21] = 1
for i in range(22, 31):
    dp[i] = dp[i - 5] + dp[i - 2] + dp[i - 1]
print(dp)
