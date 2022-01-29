dp = [0] * 43
dp[3] = 1
for i in range(4, 43):
    if i % 2 == 0:
        dp[i] = dp[i - 3] + dp[i // 2]
    else:
        dp[i] = dp[i - 3]
print(dp)
