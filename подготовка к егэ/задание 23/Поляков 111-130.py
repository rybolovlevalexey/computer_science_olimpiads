dp = [0] * 228
dp[1] = 1
program = {1: ['']}
for i in range(2, 228):
    program[i] = []
    if i % 3 == 0 and i - 5 >= 1:
        dp[i] = dp[i - 1] + dp[i - 5] + dp[i // 3]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i - 5]:
            program[i] += [elem + '2']
        for elem in program[i // 3]:
            program[i] += [elem + '3']
    elif i % 3 == 0:
        dp[i] = dp[i - 1] + dp[i // 3]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i // 3]:
            program[i] += [elem + '3']
    elif i - 5 >= 1:
        dp[i] = dp[i - 1] + dp[i - 5]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
        for elem in program[i - 5]:
            program[i] += [elem + '2']
    else:
        dp[i] = dp[i - 1]
        for elem in program[i - 1]:
            program[i] += [elem + '1']
    program[i] = [min(program[i], key=lambda x: len(x))]
print(dp)
print(program)
print(len(program[227][0]))