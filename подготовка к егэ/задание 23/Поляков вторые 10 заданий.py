dp = [0] * 25
dp[1] = 1
for i in range(2, 25):
    if i % 2 == 0:
        dp[i] = dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 2]
print(dp)