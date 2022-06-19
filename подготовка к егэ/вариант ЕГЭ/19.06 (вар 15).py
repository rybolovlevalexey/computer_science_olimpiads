def convert(x, q):
    st = ''
    while x > 0:
        st += str(x % q)
        x //= q
    return st[::-1]

num = int('65', 8)
for i in range(2, 15):
    if convert(num, i) == '311':
        print(i)
print(int('311', 4))
print(int('65', 8))