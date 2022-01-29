dp = [0] * 50
dp[1] = 1
for i in range(2, 50):
    if i % 3 == 0 and i - 2 >= 0:
        dp[i] = dp[i // 3] + dp[i - 2]
    elif i - 2 >= 0:
        dp[i] = dp[i - 2]
    else:
        dp[i] = dp[i // 3]
print(dp)
