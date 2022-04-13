dp = [0] * 21
dp[3] = 1
for i in range(4, 16):
    if i == 10:
        continue
    if 0 <= i - 3 <= 20:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(15):
    dp[i] = 0
print(dp)
for i in range(16, 21):
    if 0 <= i - 3 <= 20:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)