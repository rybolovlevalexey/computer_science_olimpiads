dp = [0] * 27
dp[2] = 1
for i in range(3, 16):
    if i == 10:
        continue
    if i - 5 >= 0:
        dp[i] = dp[i - 1] + dp[i - 5]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(15):
    dp[i] = 0
print(dp)
for i in range(16, 27):
    if i - 5 >= 0:
        dp[i] = dp[i - 1] + dp[i - 5]
    else:
        dp[i] = dp[i - 1]
print(dp)