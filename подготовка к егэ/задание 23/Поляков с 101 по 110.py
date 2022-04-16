ways = {1: ['']}
dp = [0] * 21
dp[1] = 1
for i in range(2, 21):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
        ways[i] = list()
        for elem in ways.get(i - 1, []):
            ways[i] += [elem + '1']
        for elem in ways.get(i - 2, []):
            ways[i] += [elem + '2']
        for elem in ways.get(i // 2, []):
            ways[i] += [elem + '3']
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
        ways[i] = list()
        for elem in ways.get(i - 1, []):
            ways[i] += [elem + '1']
        for elem in ways.get(i - 2, []):
            ways[i] += [elem + '2']
print(dp)
print(len(ways[20]))
cnt = 0
for elem in ways[20]:
    if len(elem) == 6:
        cnt += 1
print(cnt)