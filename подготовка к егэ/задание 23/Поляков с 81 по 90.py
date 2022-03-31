dp = [0] * 14
dp[1] = 1
for i in range(2, 5):
    if i % 2 == 0 and i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(4):
    dp[i] = 0
print(dp)
for i in range(5, 10):
    if i % 2 == 0 and i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(9):
    dp[i] = 0
print(dp)
for i in range(10, 14):
    if i % 2 == 0 and i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)