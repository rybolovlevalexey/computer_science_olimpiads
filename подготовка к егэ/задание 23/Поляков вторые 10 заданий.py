dp = [0] * 33
dp[1] = 1
for i in range(2, 33):
    if i % 4 == 0:
        dp[i] = dp[i - 1] + dp[i // 4]
    else:
        dp[i] = dp[i - 1]
print(dp)
