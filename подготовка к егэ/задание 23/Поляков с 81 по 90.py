dp = [0] * 13
dp[1] = 1
for i in range(2, 8):
    if i % 2 == 0 and i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(7):
    dp[i] = 0
print(dp)
for i in range(8, 11):
    if i % 2 == 0 and i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(10):
    dp[i] = 0
print(dp)
for i in range(11, 13):
    if i % 2 == 0 and i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 2 >= 0:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]
print(dp)