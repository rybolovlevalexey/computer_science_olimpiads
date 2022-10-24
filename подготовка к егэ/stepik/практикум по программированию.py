sp = list(map(int, input().split()))
for i in range(len(sp) - 1):
    for j in range(i, len(sp) - 1):
        a = sum(list(map(int, list(str(sp[j])))))
        b = sum(list(map(int, list(str(sp[j + 1])))))
        if a > b:
            sp[j], sp[j + 1] = sp[j + 1], sp[j]
        if a == b and sp[j] > sp[j + 1]:
            sp[j], sp[j + 1] = sp[j + 1], sp[j]
print(*sp)
