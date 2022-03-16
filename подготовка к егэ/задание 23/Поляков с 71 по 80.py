dp = [0] * 13
dp[2] = 1
for i in range(3, 13):
    if i == 10:
        continue
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
