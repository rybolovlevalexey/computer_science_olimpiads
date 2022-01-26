dp = [0] * 28
dp[11] = 1
for i in range(12, 28):
    if i - 10 >= 0:
        dp[i] = dp[i - 1] + dp[i - 10]
    else:
        dp[i] = dp[i - 1]
print(dp)