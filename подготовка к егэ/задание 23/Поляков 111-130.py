dp = [0] * 24
dp[4] = 1
for i in range(5, 9):
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(8):
    dp[i] = 0
print(dp)
for i in range(9, 24):
    if i == 11 or i == 18:
        continue
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)