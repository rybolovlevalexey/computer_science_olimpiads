dp = [0] * 16
dp[3] = 1
for i in range(4, 16):
    if i == 8:
        continue
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp)