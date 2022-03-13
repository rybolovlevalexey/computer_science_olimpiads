dp = [0] * 34
dp[2] = 1
for i in range(3, 17):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]

print(dp)
for i in range(16):
    dp[i] = 0
print(dp)
for i in range(17, 34):
    if i == 30:
        continue
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)