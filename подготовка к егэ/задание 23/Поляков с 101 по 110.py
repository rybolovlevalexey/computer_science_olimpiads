dp = [0] * 22
dp[2] = 1
for i in range(3, 6):
    if i - 2 >= 0 and i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(5):
    dp[i] = 0
print(dp)
for i in range(6, 22):
    if i == 8 or i == 11:
        continue
    if i - 2 >= 0 and i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
print(dp[21])