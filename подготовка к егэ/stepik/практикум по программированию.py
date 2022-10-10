ans = set()
st = input().split()
for elem in st:
    elem = int(elem)
    if elem in ans:
        print('YES')
    else:
        print('NO')
        ans.add(elem)