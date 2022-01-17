dp = [0] * 90
for i in range(4, 90):
    if i % 6 == 0:
        dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i - 1], dp[i // 3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i - 1], dp[i // 2]) + 1
    else:
        dp[i] = dp[i - 1] + 1
print(dp)