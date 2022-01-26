dp = [0] * 28
dp[2] = 1
for i in range(3, 28):
    if i % 2 == 0 and int(i ** 0.5) == i ** 0.5:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[int(i ** 0.5)]
    elif i % 2 != 0 and int(i ** 0.5) == i ** 0.5:
        dp[i] = dp[i - 1] + dp[int(i ** 0.5)]
    elif i % 2 == 0 and int(i ** 0.5) != i ** 0.5:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)