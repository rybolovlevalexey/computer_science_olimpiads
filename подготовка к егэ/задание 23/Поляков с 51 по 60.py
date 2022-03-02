dp = [0] * 41
dp[2] = 1
for i in range(3, 21):
    if i == 8:
        continue
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(20):
    dp[i] = 0
print(dp)
for i in range(21, 41):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)