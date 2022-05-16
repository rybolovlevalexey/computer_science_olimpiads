dp = [0] * 100
dp[5] = 1
for i in range(6, len(dp)):
    dp[i] = dp[i - 2] + dp[i - 5]

    if dp[i] == 34:
        print(i)
        break
