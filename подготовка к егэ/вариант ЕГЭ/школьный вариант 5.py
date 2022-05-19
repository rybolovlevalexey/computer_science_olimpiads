dp = [0] * 101
dp[10] = 1
for i in range(11, 66):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[(i - 1) // 2]
print(dp)
for i in range(65):
    dp[i] = 0
print(dp)
for i in range(66, 101):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1] + dp[(i - 1) // 2]
print(dp)
