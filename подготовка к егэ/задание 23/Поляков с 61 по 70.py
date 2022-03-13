dp = [0] * 64
dp[1] = 1
for i in range(2, 26):
    if i == 6:
        continue
    if i % 3 == 0:
        dp[i] = dp[i // 3] + dp[i - 2]
    else:
        dp[i] = dp[i - 2]
print(dp)
for i in range(25):
    dp[i] = 0
print(dp)
for i in range(26, 64):
    if i % 3 == 0:
        dp[i] = dp[i // 3] + dp[i - 2]
    else:
        dp[i] = dp[i - 2]
print(dp)