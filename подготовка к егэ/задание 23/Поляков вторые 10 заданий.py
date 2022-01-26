dp = [0] * 20
dp[2] = 1
for i in range(3, 20):
    if i - 3 >= 0 and int(i ** 0.5) == i ** 0.5:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[int(i ** 0.5)]
    elif i - 3 >= 0 and int(i ** 0.5) != i ** 0.5:
        dp[i] = dp[i - 1] + dp[i - 3]
    elif i - 3 < 0 and int(i ** 0.5) == i ** 0.5:
        dp[i] = dp[i - 1] + dp[int(i ** 0.5)]
    else:
        dp[i] = dp[i - 1]
print(dp)