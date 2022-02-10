dp = [0] * 21
dp[3] = 1
for i in range(4, 13):
    dp[i] = dp[i - 1] + dp[i - 3]
print(dp)
for i in range(0, 12):
    dp[i] = 0
print(dp)
for i in range(13, 21):
    dp[i] = dp[i - 1] + dp[i - 3]
print(dp)