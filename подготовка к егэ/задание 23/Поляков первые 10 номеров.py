dp = [0] * 16
dp[1] = 1
for i in range(2, 16):
    if i >= 3 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i >= 3:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
