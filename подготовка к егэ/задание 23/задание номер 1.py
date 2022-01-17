dp = [0] * 10
i = 2
while True:
    if (i - 1) % 2 == 0:
        dp[i] = max(dp[i - 3], dp[(i - 1) // 2]) + 1
    else:
        dp[i] = dp[i - 3] + 1
    dp.append(0)
    if dp[i - 3] > 13 and dp[(i - 1) // 2] > 13:
        break
    i += 1
print(len(dp))
print(dp)
print(dp.count(13))