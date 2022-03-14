dp = [0] * 14
dp[1] = 1
for i in range(2, 8):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(7):
    dp[i] = 0
print(dp)
for i in range(8, 14):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp)