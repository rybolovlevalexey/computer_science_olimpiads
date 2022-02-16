dp = [0] * 11
dp[2] = 1
for i in range(3, 11):
    if i - 3 >= 0 and (i + 1) % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[(i + 1) // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    elif (i + 1) % 2 == 0:
        dp[i] = dp[i - 1] + dp[(i + 1) // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)