dp = [0] * 28
dp[3] = 1
deyst = {3: ['']}
for i in range(4, 28):
    deyst[i] = list()
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 4] + dp[i // 2]
        for elem in deyst.get(i - 1, []):
            deyst[i] += [elem + '1']
        for elem in deyst.get(i - 4, []):
            deyst[i] += [elem + '2']
        for elem in deyst.get(i // 2, []):
            deyst[i] += [elem + '3']
    else:
        dp[i] = dp[i - 1] + dp[i - 4]
        for elem in deyst.get(i - 1, []):
            deyst[i] += [elem + '1']
        for elem in deyst.get(i - 4, []):
            deyst[i] += [elem + '2']
print(dp)
print(len(deyst[27]))
cnt = 0
for elem in deyst[27]:
    if len(elem) == 7:
        cnt += 1
print(cnt)
