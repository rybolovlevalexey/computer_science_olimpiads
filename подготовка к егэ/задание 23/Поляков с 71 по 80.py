dp = [0] * 14
dp[3] = 1
for i in range(4, 14):
    if i == 8:
        continue
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
