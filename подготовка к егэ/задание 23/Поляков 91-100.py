dp = [0] * 53
dp[5] = 1
for i in range(6, 16):
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]
for i in range(15):
    dp[i] = 0
for i in range(16, 53):
    if i == 29:
        continue
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]
print(dp)