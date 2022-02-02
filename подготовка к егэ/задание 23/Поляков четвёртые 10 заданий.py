dp = [0] * 56
dp[1] = 1
for i in range(2, 56):
    if i - 2 >= 0 and i % 3 == 0:
        dp[i] = dp[i - 2] + dp[i // 3]
    elif i % 3 == 0:
        dp[i] = dp[i // 3]
    elif i - 2 >= 0:
        dp[i] = dp[i - 2]
print(dp)
