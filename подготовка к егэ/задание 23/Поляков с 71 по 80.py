dp = [0] * 17
dp[2] = 1
for i in range(3, 17):
    if i == 14:
        continue
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
