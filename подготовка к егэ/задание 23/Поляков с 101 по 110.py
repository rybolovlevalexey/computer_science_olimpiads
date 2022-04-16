ways = {3: ['']}
dp = [0] * 23
dp[3] = 1
for i in range(4, 23):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    ways[i] = list()
    for elem in ways.get(i - 1, []):
        ways[i] += [elem + '1']
    for elem in ways.get(i - 2, []):
        ways[i] += [elem + '2']
    for elem in ways.get(i - 3, []):
        ways[i] += [elem + '3']

print(dp)
print(len(ways[22]))
cnt = 0
for elem in ways[22]:
    if len(elem) == 7:
        cnt += 1
print(cnt)