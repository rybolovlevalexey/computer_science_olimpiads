dp = [0] * 61
dp[5] = 1
for i in range(6, 9):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(8):
    dp[i] = 0
print(dp)
for i in range(9, 61):
    if i == 22:
        continue
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)