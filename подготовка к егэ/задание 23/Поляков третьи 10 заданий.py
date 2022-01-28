dp = [0] * 47
dp[24] = 1
for i in range(25, 47):
    if i % 10 == 9:
        dp[i] = dp[i - 1] + dp[i - 10]
    else:
        dp[i] = dp[i - 1] + dp[i - 11]
print(dp)