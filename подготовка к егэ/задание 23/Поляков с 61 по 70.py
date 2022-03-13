dp = [0] * 56
dp[3] = 1
for i in range(4, 19):
    if i == 12:
        continue
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(18):
    dp[i] = 0
print(dp)
for i in range(19, 56):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)