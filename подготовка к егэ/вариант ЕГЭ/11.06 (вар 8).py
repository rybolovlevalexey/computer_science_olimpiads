dp = [0] * 21
dp[1] = 1
for i in range(2, 21):
    if i - 5 >= 0:
        dp[i] = dp[i - 2] + dp[i - 5]
    else:
        dp[i] = dp[i - 2]
print(dp)