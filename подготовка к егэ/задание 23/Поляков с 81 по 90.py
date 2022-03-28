dp = [0] * 26
dp[1] = 1
for i in range(2, 26):
    if i == 21:
        continue
    if (i - 1) % 2 == 0:
        dp[i] = dp[i - 1] + dp[(i - 1) // 2]
    else:
        dp[i] = dp[i - 1]
print(dp)