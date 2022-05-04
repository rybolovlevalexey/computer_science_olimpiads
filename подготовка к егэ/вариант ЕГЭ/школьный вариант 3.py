dp = [0] * 65
dp[2] = 1
for i in range(3, 65):
    if i == 8:
        continue
    if int(i ** 0.5) == i**0.5 and i % 2 == 0:
        dp[i] = dp[i - 2] + dp[i // 2] + dp[int(i ** 0.5)]
    elif i % 2 == 0:
        dp[i] = dp[i - 2] + dp[i // 2]
    elif int(i ** 0.5) == i**0.5:
        dp[i] = dp[i - 2] + dp[int(i ** 0.5)]
    else:
        dp[i] = dp[i - 2]
print(dp)