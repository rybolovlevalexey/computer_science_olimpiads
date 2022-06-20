def isprost(x):
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            return False
    return True

k = 0
num = 670_001
while k < 5:
    s = 0
    for d in range(2, int(num**0.5)+1):
        if num % d == 0:
            if isprost(d):
                s += d
            if isprost(num // d):
                s += num // d
    if s % 10 == 5:
        print(num, s)
        k += 1
    num += 1
