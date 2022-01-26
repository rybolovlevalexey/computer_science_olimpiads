dp = [0] * 50
dp[5] = 1
for i in range(6, 50):
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]
print(dp)