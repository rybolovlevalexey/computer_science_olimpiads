dp = [0] * 21
dp[3] = 1
num_sp = {3: ['']}
for i in range(4, 21):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i - 1]
        num_sp[i] = list()
        for elem in num_sp.get(i - 1, []):
            num_sp[i].append(elem + '1')
        for elem in num_sp.get(i // 2, []):
            num_sp[i].append(elem + '2')
    else:
        dp[i] = dp[i - 1]
        num_sp[i] = list()
        for elem in num_sp.get(i - 1, []):
            num_sp[i].append(elem + '1')
print(dp)
for key, value in num_sp.items():
    print(key, value)
print(len(num_sp[20]))
ans = 0
for i in range(len(num_sp[20])):
    elem = num_sp[20][i]
    print(elem)
    if elem[-2] == '1':
        ans += 1
print(ans)