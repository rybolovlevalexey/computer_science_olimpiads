ways = {2: ['']}
dp = [0] * 26
dp[2] = 1
for i in range(3, 26):
    ways[i] = list()
    if i % 2 == 0 and 0 <= i - 3 <= 25:
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i // 2]
        for elem in ways.get(i - 1, []):
            ways[i] += [elem + '1']
        for elem in ways.get(i - 3, []):
            ways[i] += [elem + '2']
        for elem in ways.get(i // 2, []):
            ways[i] += [elem + '3']
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
        for elem in ways.get(i - 1, []):
            ways[i] += [elem + '1']
        for elem in ways.get(i // 2, []):
            ways[i] += [elem + '3']
    elif 0 <= i - 3 <= 25:
        dp[i] = dp[i - 1] + dp[i - 3]
        for elem in ways.get(i - 1, []):
            ways[i] += [elem + '1']
        for elem in ways.get(i - 3, []):
            ways[i] += [elem + '2']
    else:
        dp[i] = dp[i - 1]
        for elem in ways.get(i - 1, []):
            ways[i] += [elem + '1']

print(dp)
print(len(ways[25]))
cnt = 0
for elem in ways[25]:
    if len(elem) == 7:
        cnt += 1
print(cnt)