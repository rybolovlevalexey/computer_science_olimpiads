n = int(input())
flag = True
check = None
sp = list()
for i in range(n):
    line = list(map(int, input().split()))
    if check is None:
        check = sum(line)
    if check != sum(line):
        flag = False
    sp.append(line)
s1 = 0
s2 = 0
for j in range(n):
    s1 += sp[j][j]
    s2 += sp[j][n - j - 1]
if s1 != check or s2 != check:
    flag = False
numbers = set()
for j in range(n):
    s = 0
    for i in range(n):
        s += sp[i][j]
        numbers.add(sp[i][j])
    if s != check:
        flag = False
if len(numbers) != n**2:
    flag = False
if not flag:
    print("NO")
else:
    numbers = sorted(numbers)
    for i in range(n**2):
        if numbers[i] != i + 1:
            flag = False
            break
    print("YES" if flag else "NO")