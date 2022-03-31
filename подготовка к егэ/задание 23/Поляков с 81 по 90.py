dp = [0] * 29
dp[2] = 1
for i in range(3, 13):
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
for i in range(12):
    dp[i] = 0
for i in range(13, 29):
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)