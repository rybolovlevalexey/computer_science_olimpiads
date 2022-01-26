dp = [0] * 16
dp[3] = 1
for i in range(4, 16):
    if i - 3 >= 0 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i - 3 >= 0 and i % 2 != 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    elif i - 3 < 0 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)