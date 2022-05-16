dp = [0] * 1000
dp[1] = 1
for i in range(2, len(dp)):
    if i - 5 >= 0 and i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 5] + dp[i // 3]
    elif i - 5 >= 0:
        dp[i] = dp[i - 1] + dp[i - 5]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]

    if dp[i] == 175:
        print(i)
        break