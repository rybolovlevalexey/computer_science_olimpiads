dp = [0] * 32
dp[2] = 1
for i in range(3, 16):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]

print(dp)
for i in range(15):
    dp[i] = 0
print(dp)
for i in range(16, 32):
    if i == 22:
        continue
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)