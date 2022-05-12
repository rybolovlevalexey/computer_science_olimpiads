dp = [0] * 29
dp[1] = 1
program = {1: ['']}
for i in range(2, 29):
    program[i] = []
    if i - 2 >= 1 and i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i // 2]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i - 2]:
            program[i] += [elem + '2']
        for elem in program[i // 2]:
            program[i] += [elem + '3']
    elif i - 2 >= 1:
        dp[i] = dp[i - 1] + dp[i - 2]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i - 2]:
            program[i] += [elem + '2']
    elif i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i // 2]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i // 2]:
            program[i] += [elem + '3']
    else:
        dp[i] = dp[i - 1]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
print(dp)
mndl = len(min(program[28], key=lambda x: len(x)))
print(mndl)
cnt = 0
for elem in program[28]:
    if len(elem) == mndl:
        cnt += 1
print(cnt)