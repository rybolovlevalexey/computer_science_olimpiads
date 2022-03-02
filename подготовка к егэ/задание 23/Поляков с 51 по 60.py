dp = [0] * 31
dp[3] = 1
for i in range(4, 21):
    if i == 12:
        continue
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(20):
    dp[i] = 0
print(dp)
for i in range(21, 31):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)