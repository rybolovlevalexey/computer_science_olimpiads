# 12 25
dp = [0] * 41
dp[1] = 1
for i in range(2, 13):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(12):
    dp[i] = 0
print(dp)
for i in range(13, 26):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(25):
    dp[i] = 0
print(dp)
for i in range(26, 41):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)