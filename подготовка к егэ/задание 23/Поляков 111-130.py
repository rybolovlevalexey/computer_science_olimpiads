dp = [0] * 27
dp[5] = 1
for i in range(6, 12):
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(11):
    dp[i] = 0
print(dp)
for i in range(12, 27):
    if i == 13 or i == 15:
        continue
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)