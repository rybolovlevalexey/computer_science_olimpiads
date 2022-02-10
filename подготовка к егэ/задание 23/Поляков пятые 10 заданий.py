dp = [0] * 16
dp[4] = 1
for i in range(5, 9):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp)
for i in range(0, 8):
    dp[i] = 0
print(dp)
for i in range(9, 16):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp)