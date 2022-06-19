dp = [0] * 66
dp[2] = 1
for i in range(3, 17):
    if i % 12 == 0:
        dp[i] = dp[i - 1] + dp[i // 3] + dp[i // 4]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i // 4]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(16):
    dp[i] = 0
print(dp)
for i in range(17, 66):
    if i == 21:
        continue
    if i % 12 == 0:
        dp[i] = dp[i - 1] + dp[i // 3] + dp[i // 4]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i // 4]
    else:
        dp[i] = dp[i - 1]
print(dp)