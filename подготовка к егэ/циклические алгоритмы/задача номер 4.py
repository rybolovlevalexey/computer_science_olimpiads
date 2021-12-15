answer = 0
maximum = 0
for i in range(333666, 666999 + 1):
    if str(i).count('7') >= 2 and i % 17 == 0:
        answer += 1
        maximum = i
print(answer, maximum)
