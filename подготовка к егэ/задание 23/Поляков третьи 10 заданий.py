dp = [0] * 50
dp[26] = 1
for i in range(27, 50):
    if i % 10 == 9:
        dp[i] = dp[i - 1] + dp[i - 10]
    else:
        dp[i] = dp[i - 1] + dp[i - 11]
print(dp)