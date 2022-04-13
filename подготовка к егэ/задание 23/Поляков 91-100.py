dp = [0] * 21
dp[2] = 1
for i in range(3, 11):
    if 0 <= i - 3 <= 20:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
for i in range(10):
    dp[i] = 0
print(dp)
for i in range(11, 21):
    if i == 15:
        continue
    if 0 <= i - 3 <= 20:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)