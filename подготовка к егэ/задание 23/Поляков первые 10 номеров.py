dp = [0] * 18
dp[1] = 1
for i in range(2, 18):
    if i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 4]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)