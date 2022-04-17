dp = [0] * 29
dp[1] = 1
for i in range(2, 9):
    if i - 2 >= 0 and i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 3]
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
    elif i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(8):
    dp[i] = 0
print(dp)
for i in range(9, 29):
    if i == 10 or i == 11:
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
print(dp[28])