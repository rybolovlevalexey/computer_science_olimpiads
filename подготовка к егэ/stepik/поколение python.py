n = int(input())
num = 1
cnt = 1
while True:
    if cnt + len(str(num)) > n:
        st = str(num)[::-1]
        while cnt < n:
            st = st[1:]
            cnt += 1
        print(st[0])
        break
    cnt += len(str(num))
    num += 1
