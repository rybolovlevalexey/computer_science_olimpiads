dp = [0] * 19
dp[3] = 1
num_sp = {3: ['']}
for i in range(4, 19):
    dp[i] = dp[i - 1] + dp[i - 2]
    num_sp[i] = list()
    for elem in num_sp.get(i - 1, []):
        num_sp[i] += [elem + '1']
    for elem in num_sp.get(i - 2, []):
        num_sp[i] += [elem + '2']

ans = 0
for elem in num_sp[18]:
    if elem[-2] == '2':
        ans += 1
print(ans)