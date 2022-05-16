dp = [0] * 100000
dp[31] = 1
for i in range(32, len(dp)):
    dp[i] = dp[i - 2] + dp[i - 5] + dp[i - 4]

    if dp[i] == 1001:
        print(i)
        break
