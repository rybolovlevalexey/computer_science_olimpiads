dp = [0] * 21
dp[3] = 1
for i in range(4, 10):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
for i in range(9):
    dp[i] = 0
print(dp)
for i in range(10, 21):
    if i == 15:
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp)
