dp = [0] * 31
dp[1] = 1
for i in range(2, 11):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(10):
    dp[i] = 0
print(dp)
for i in range(11, 22):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(21):
    dp[i] = 0
print(dp)
for i in range(22, 31):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
print(dp)
