dp = [0] * 17
dp[1] = 1
for i in range(2, 17):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)