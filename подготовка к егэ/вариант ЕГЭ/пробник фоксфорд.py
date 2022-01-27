dp = [0] * 23
dp[5] = 1
for i in range(6, 12):
    dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]
print(dp)
res = dp[11]
dp[:11] = [0] * 11
print(dp)
for i in range(12, 23):
    if i == 14:
        continue
    dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]
print(dp)
print(dp[-1])