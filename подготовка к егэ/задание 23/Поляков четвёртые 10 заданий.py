dp = [0] * 47
dp[30] = 1
for i in range(31, 47):
    dp[i] = dp[i - 1] + dp[i - 4] + dp[i - 5]
print(dp)
