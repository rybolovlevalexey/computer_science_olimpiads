dp = [0] * 19
dp[1] = 1
for i in range(2, 19):
    if i >= 3 and i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 4]
    elif i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i // 4]
    elif i >= 3:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
