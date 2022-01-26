dp = [0] * 28
dp[5] = 1
for i in range(6, 28):
    if i % 3 == 0 and i - 3 >= 0:
        dp[i] = dp[i - 3] + dp[i // 3]
    elif i - 3 >= 0:
        dp[i] = dp[i - 3]
    elif i % 3 == 0:
        dp[i] = dp[i // 3]
print(dp)
