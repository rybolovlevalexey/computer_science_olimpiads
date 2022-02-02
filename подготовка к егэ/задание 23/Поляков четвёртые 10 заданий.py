dp = [0] * 23
dp[2] = 1
for i in range(3, 23):
    if i % 1.5 == 0:
        dp[i] = dp[i - 1] + dp[int(i // 1.5)]
    else:
        dp[i] = dp[i - 1]
print(dp)
