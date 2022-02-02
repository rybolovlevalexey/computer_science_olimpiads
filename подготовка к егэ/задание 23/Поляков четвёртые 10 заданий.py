dp = [0] * 17
dp[2] = 1
for i in range(3, 17):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[(i - 1) // 2]
print(dp)
