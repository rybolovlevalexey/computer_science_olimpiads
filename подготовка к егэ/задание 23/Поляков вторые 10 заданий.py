dp = [0] * 37
dp[12] = 1
for i in range(13, 37):
    if i - 10 >= 0:
        dp[i] = dp[i - 1] + dp[i - 10]
    else:
        dp[i] = dp[i - 1]
print(dp)