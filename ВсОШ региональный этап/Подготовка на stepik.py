dictionary = {0: 0, 1: 1}


def func(n):
    if n == 0 or n == 1:
        return n
    elif n >= 2 and n in dictionary:
        return dictionary[n]
    else:
        res = func(n - 1) + func(n - 2)
        dictionary[n] = res
        return res


number = int(input())
print(func(number))
