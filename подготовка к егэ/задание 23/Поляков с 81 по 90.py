dp = [0] * 14
dp[2] = 1
for i in range(3, 14):
    if i == 6:
        continue
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 4]
print(dp)