dp = [0] * 35
dp[4] = 1
for i in range(5, 11):
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(10):
    dp[i] = 0
print(dp)
for i in range(11, 35):
    if i == 18:
        continue
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    else:
        dp[i] = dp[i - 1]
print(dp)