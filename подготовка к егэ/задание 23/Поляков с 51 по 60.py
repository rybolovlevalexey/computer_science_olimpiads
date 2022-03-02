dp = [0] * 35
dp[2] = 1
for i in range(3, 13):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(12):
    dp[i] = 0
print(dp)
for i in range(13, 35):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)