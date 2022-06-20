dp = [0] * 16
dp[4] = 1
for i in range(5, 10):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(9):
    dp[i] = 0
print(dp)
for i in range(10, 13):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(12):
    dp[i] = 0
print(dp)
for i in range(13, 16):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)