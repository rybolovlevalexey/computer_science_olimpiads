dp = [0] * 15
dp[2] = 1
for i in range(3, 7):
    if i - 3 >= 0 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(6):
    dp[i] = 0
print(dp)
for i in range(7, 11):
    if i - 3 >= 0 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(10):
    dp[i] = 0
print(dp)
for i in range(11, 15):
    if i - 3 >= 0 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
