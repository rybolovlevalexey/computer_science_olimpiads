dp = [0] * 35
dp[1] = 1
deyst = {1: ['']}
for i in range(2, 35):
    deyst[i] = list()
    if i % 6 == 0:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i // 3]
        for elem in deyst.get(i - 1, []):
            deyst[i] += [elem + '1']
        for elem in deyst.get(i // 2, []):
            deyst[i] += [elem + '2']
        for elem in deyst.get(i // 3, []):
            deyst[i] += [elem + '3']
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
        for elem in deyst.get(i - 1, []):
            deyst[i] += [elem + '1']
        for elem in deyst.get(i // 2, []):
            deyst[i] += [elem + '2']
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
        for elem in deyst.get(i - 1, []):
            deyst[i] += [elem + '1']
        for elem in deyst.get(i // 3, []):
            deyst[i] += [elem + '3']
    else:
        dp[i] = dp[i - 1]
        for elem in deyst.get(i - 1, []):
            deyst[i] += [elem + '1']
print(dp)
print(len(deyst[34]))
cnt = 0
for elem in deyst[34]:
    if len(elem) == 8:
        cnt += 1
print(cnt)
