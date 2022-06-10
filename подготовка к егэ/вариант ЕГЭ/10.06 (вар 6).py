def isprost(x):
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            return False
    return True


n = 1
for num in range(245690, 245756+1):
    if isprost(num):
        print(n, num)
    n += 1
