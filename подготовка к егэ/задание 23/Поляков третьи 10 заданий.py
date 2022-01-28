dp = [0] * 52
dp[25] = 1
for i in range(26, 52):
    if i % 10 == 9:
        dp[i] = dp[i - 1] + dp[i - 10]
    else:
        dp[i] = dp[i - 1] + dp[i - 11]
print(dp)