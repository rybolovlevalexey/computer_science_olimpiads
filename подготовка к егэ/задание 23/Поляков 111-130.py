dp = [0] * 112
dp[1] = 1
program = {1: ['']}
for i in range(2, 112):
    program[i] = []
    if i - 5 >= 1 and i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i - 5] + dp[i // 3]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i - 5]:
            program[i] += [elem + '2']
        for elem in program[i // 3]:
            program[i] += [elem + '3']
    elif i - 5 >= 1:
        dp[i] = dp[i - 1] + dp[i - 5]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i - 5]:
            program[i] += [elem + '2']
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i // 3]:
            program[i] += [elem + '3']
    else:
        dp[i] = dp[i - 1]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
    if i != 111:
        mndl = len(min(program[i], key=lambda x: len(x)))
        sp = list()
        for elem in program[i]:
            if len(elem) == mndl:
                sp.append(elem)
        program[i] = sp
print(dp)
mndl = len(min(program[111], key=lambda x: len(x)))
print(mndl)
cnt = 0
for elem in program[111]:
    if len(elem) == mndl:
        cnt += 1
        print(elem)
print(cnt)