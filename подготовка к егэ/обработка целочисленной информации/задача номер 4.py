def is_prost(num):
    for d in range(2, num // 2 + 1):
        if num % d == 0 and num != d:
            return False
    return True


def all_delit(num):
    sp = list()
    for d1 in range(2, num // 2 + 1):
        if num % d1 == 0 and is_prost(d1):
            flag = False
            d2 = 1
            for d2 in range(num // 10):
                d2 = int(str(d2) + str(d1)[-1])
                if num % d2 == 0 and is_prost(d2):
                    flag = True
            if not flag:
                return False
            d3 = num // (d1 * d2)
            if is_prost(d3) and str(d3)[-1] == str(d2)[-1] == str(d1)[-1]:
                return True
            return False
    return False


answer = 0
minimum = -1
for elem in range(318216, 369453 + 1):
    if all_delit(elem):
        answer += 1
        if minimum == -1:
            minimum = elem
print(answer, minimum)