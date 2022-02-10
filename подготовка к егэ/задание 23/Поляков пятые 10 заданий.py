dp = [0] * 16
dp[5] = 1
for i in range(6, 11):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(0, 10):
    dp[i] = 0
print(dp)
for i in range(11, 16):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp)