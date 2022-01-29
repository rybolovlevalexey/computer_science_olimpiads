dp = [0] * 21
dp[7] = 1
for i in range(8, 21):
    if i - 3 >= 0:
        dp[i] = dp[i - 1] + dp[i - 3]
    else:
        dp[i] = dp[i - 1]
print(dp)
