ams = None
for num in range(1, 1000):
    if num % 16 !=0:
        continue
    st = bin(num)[2:][::-1]
    cnt = 0
    while st[0] == '0':
        cnt += 1
        st = st[1:]
    if ams is None or cnt < ams:
        ams = cnt
print(ams)