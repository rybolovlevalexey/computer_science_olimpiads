dp = [0] * 16
dp[1] = 1
for i in range(2, 9):
    if i - 3 > 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(8):
    dp[i] = 0
print(dp)
for i in range(9, 16):
    if i - 3 > 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
