dp = [0] * 15
dp[4] = 1
num_sp = {4: ['']}
for i in range(5, 15):
    dp[i] = dp[i - 1] + dp[i - 2]
    num_sp[i] = list()
    for elem in num_sp.get(i - 1, []):
        num_sp[i] += [elem + '1']
    for elem in num_sp.get(i - 2, []):
        num_sp[i] += [elem + '2']

ans = 0
for elem in num_sp[14]:
    if elem[-2] == '1':
        ans += 1
print(ans)