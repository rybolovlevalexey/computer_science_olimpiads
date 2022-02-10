dp = [0] * 21
dp[4] = 1
for i in range(5, 11):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 3]
for i in range(0, 10):
    dp[i] = 0
for i in range(11, 21):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 3]
print(dp)