dp = [0] * 23
dp[2] = 1
for i in range(3, 12):
    if i % 2 == 0:
        dp[i] = dp[i - 2] + dp[i - 3] + dp[i // 2]
    else:
        dp[i] = dp[i - 2] + dp[i - 3]
print(dp)
for i in range(11):
    dp[i] = 0
print(dp)
for i in range(12, 23):
    if i % 2 == 0:
        dp[i] = dp[i - 2] + dp[i - 3] + dp[i // 2]
    else:
        dp[i] = dp[i - 2] + dp[i - 3]
print(dp)
