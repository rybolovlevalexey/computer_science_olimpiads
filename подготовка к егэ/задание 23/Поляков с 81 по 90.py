dp = [0] * 14
dp[3] = 1
for i in range(4, 10):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(9):
    dp[i] = 0
print(dp)
for i in range(10, 12):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(11):
    dp[i] = 0
print(dp)
for i in range(12, 14):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)