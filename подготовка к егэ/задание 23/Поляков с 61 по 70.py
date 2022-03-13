dp = [0] * 46
dp[3] = 1
for i in range(4, 11):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(10):
    dp[i] = 0
print(dp)
for i in range(11, 46):
    if i == 15:
        continue
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)