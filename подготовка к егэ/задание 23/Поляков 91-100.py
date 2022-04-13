dp = [0] * 19
dp[2] = 1
for i in range(3, 10):
    if 0 <= i - 3 <= 19:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(9):
    dp[i] = 0
print(dp)
for i in range(10, 19):
    if i == 14:
        continue
    if 0 <= i - 3 <= 19:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)