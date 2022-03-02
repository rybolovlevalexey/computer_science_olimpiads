dp = [0] * 51
dp[4] = 1
for i in range(5, 7):
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(6):
    dp[i] = 0
print(dp)
for i in range(7, 51):
    if i == 12:
        continue
    if i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]
print(dp)