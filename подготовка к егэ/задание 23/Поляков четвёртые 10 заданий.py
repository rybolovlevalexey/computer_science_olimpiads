dp = [0] * 52
dp[31] = 1
for i in range(32, 52):
    dp[i] = dp[i - 2] + dp[i - 4] + dp[i - 5]
print(dp)
