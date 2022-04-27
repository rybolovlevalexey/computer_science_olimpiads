dp = [0] * 32
dp[1] = 1
for i in range(2, 32):
    if i == 25:
        continue
    if (i - 1) % 2 == 0:
        dp[i] = dp[(i - 1) // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)