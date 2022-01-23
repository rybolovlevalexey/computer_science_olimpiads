def system(x, i):
    st = ''
    while x > 0:
        st += str(x % i)
        x //= i
    return st[::-1]

for n in range(100):
    if len(system(n, 6)) == 2 and len(system(n, 5)) == 3 and n % 11 == 1:
        print(n)
        break
