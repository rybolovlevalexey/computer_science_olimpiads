dp = [0] * 21
dp[3] = 1
for i in range(4, 10):
    if i - 3 >= 0 and i % 2 == 0:
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
for i in range(10, 13):
    if i - 3 >= 0 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(12):
    dp[i] = 0
print(dp)
for i in range(13, 21):
    if i - 3 >= 0 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
    elif i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
