dp = [0] * 29
dp[1] = 1
for i in range(2, 26):
    if i == 10:
        continue
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(25):
    dp[i] = 0
print(dp)
for i in range(26, 29):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)