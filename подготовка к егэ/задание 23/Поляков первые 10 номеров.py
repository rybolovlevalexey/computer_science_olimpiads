dp = [0] * 13
dp[1] = 1
for i in range(2, 13):
    if i > 2 and i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    elif i > 2 and i % 3 != 0:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]
print(dp)