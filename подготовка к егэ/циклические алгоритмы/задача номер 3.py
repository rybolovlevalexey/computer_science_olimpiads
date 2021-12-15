def is_prost(chislo):
    flag = True
    for d in range(2, chislo // 2 + 1):
        if chislo % d == 0:
            flag = False
            break
    return flag


def func(x):
    d = 2
    while x > 1:
        if x % d == 0:
            if not is_prost(d):
                return False
            x //= d
            if not is_prost(x):
                return False
            if x % 10 == 3 and d % 10 == 3:
                return True
            return False
        d += 1


answer = 0
maximum = 0
for i in range(5555, 7778):
    if func(i):
        answer += 1
        maximum = i
print(answer, maximum)
