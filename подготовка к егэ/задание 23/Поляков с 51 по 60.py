dp = [0] * 33
dp[5] = 1
num_sp = {5: ['']}
for i in range(6, 33):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
        num_sp[i] = list()
        for elem in num_sp.get(i - 1):
            if i not in num_sp:
                num_sp[i] = [elem + '1']
            else:
                num_sp[i] += [elem + '1']
        for elem in num_sp.get(i // 2, []):
            num_sp[i] += [elem + '2']
    else:
        num_sp[i] = list()
        for elem in num_sp[i - 1]:
            if i not in num_sp:
                num_sp[i] = [elem + '1']
            else:
                num_sp[i] += [elem + '1']
        dp[i] = dp[i - 1]
ans = 0
for elem in num_sp[32]:
    if elem[-2] == '1':
        ans += 1
print(ans)