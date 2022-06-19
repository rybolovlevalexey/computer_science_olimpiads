dp = [0] * 37
dp[10] = 1
for i in range(11, 19):
    if i % 2 == 0:
        dp[i] = dp[i - 2] + dp[i - 3] + dp[i // 2]
    else:
        dp[i] = dp[i - 2] + dp[i - 3]
print(dp)
for i in range(18):
    dp[i] = 0
print(dp)
for i in range(19, 37):
    if i % 2 == 0:
        dp[i] = dp[i - 2] + dp[i - 3] + dp[i // 2]
    else:
        dp[i] = dp[i - 2] + dp[i - 3]
print(dp)