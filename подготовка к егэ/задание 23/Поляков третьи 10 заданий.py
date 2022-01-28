dp = [0] * 34
dp[10] = 1
for i in range(11, 34):
    if i % 10 == 9:
        dp[i] = dp[i - 1] + dp[i - 10]
    else:
        dp[i] = dp[i - 1] + dp[i - 11]
print(dp)