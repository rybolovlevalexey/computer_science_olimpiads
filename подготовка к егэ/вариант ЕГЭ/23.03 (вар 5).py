dp = [0] * 28
dp[1] = 1
for i in range(2, 28):
    if i == 26:
        continue
    if (i - 1) % 2 == 0:
        dp[i] = dp[(i - 1) // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)