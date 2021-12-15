def func(x):
    count = 0
    for d in range(10, 21):
        if x % d == 0:
            count += 1
    if count == 5:
        return True
    return False

answer = 0
maximum = 0
for i in range(54123, 75321):
    if func(i):
        answer += 1
        maximum = i
print(answer, maximum)