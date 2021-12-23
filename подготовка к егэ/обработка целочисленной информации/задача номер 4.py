def is_prost(num):
    for d in range(2, num // 2 + 1):
        if num % d == 0 and num != d:
            return False
    return True


def all_delit(num):
    sp = list()

    for d in range(2, num // 2 + 1):
        if num % d == 0 and is_prost(d):
            if len(sp) == 0:
                sp.append(d)
            else:
                if str(sp[0])[-1] == str(d)[-1]:
                    sp.append(d)
                else:
                    return False
            num //= d
            if len(sp) > 3:
                return False
        if num == 1:
            break
    if num == 1 and len(sp) == 3 and str(sp[0])[-1] == str(sp[1])[-1] == str(sp[2])[-1]:
        return True


answer = 0
minimum = -1
for elem in range(318216, 369453 + 1):
    if all_delit(elem):
        answer += 1
        if minimum == -1:
            minimum = elem
print(answer, minimum)