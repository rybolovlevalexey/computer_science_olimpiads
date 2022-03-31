dp = [0] * 16
dp[2] = 1
for i in range(3, 5):
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(4):
    dp[i] = 0
print(dp)
for i in range(5, 12):
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(11):
    dp[i] = 0
print(dp)
for i in range(12, 16):
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp)