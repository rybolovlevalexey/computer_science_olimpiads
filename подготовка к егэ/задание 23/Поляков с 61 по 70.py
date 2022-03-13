dp = [0] * 22
dp[3] = 1
for i in range(4, 13):
    dp[i] = dp[i - 3] + dp[i - 1]
print(dp)
for i in range(12):
    dp[i] = 0
print(dp)
for i in range(13, 22):
    if i == 18:
        continue
    dp[i] = dp[i - 3] + dp[i - 1]
print(dp)