dp = [0] * 21
dp[1] = 1
for i in range(2, 21):
    if i % 1.5 == 0:
        dp[i] = dp[i - 1] + dp[int(i // 1.5)]
    else:
        dp[i] = dp[i - 1]
print(dp)
