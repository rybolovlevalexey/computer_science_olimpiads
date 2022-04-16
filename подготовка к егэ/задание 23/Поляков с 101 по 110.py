dp = [0] * 25
dp[2] = 1
for i in range(3, 7):
    if i % 4 == 0 and 0 <= i - 4 <= 24:
        dp[i] = dp[i - 1] + dp[i - 4] + dp[i // 4]
    elif i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i // 4]
    elif 0 <= i - 4 <= 24:
        dp[i] = dp[i - 1] + dp[i - 4]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(6):
    dp[i] = 0
print(dp)
for i in range(7, 25):
    if i == 8:
        continue
    if i % 4 == 0 and 0 <= i - 4 <= 24:
        dp[i] = dp[i - 1] + dp[i - 4] + dp[i // 4]
    elif i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i // 4]
    elif 0 <= i - 4 <= 24:
        dp[i] = dp[i - 1] + dp[i - 4]
    else:
        dp[i] = dp[i - 1]
print(dp)