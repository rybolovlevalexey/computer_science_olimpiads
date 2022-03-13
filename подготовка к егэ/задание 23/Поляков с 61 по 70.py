dp = [0] * 26
dp[5] = 1
for i in range(6, 16):
    if i == 12:
        continue
    dp[i] = dp[i - 3] + dp[i - 1]
print(dp)
for i in range(15):
    dp[i] = 0
print(dp)
for i in range(16, 26):
    dp[i] = dp[i - 3] + dp[i - 1]
print(dp)