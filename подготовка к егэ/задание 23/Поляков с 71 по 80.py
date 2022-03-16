dp = [0] * 32
dp[2] = 1
for i in range(3, 32):
    if i == 25:
        continue
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
