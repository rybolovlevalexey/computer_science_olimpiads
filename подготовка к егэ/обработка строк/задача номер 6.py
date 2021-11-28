file = open('24-s1.txt', 'r')
text = file.read().strip().split('\n')
ans = 0
for elem in text:
    flag = False
    for i in range(len(elem) - 2):
        i1 = elem[i]
        i2 = elem[i + 1]
        i3 = elem[i + 2]
        if i1 == 'F' and i3 == 'O':
            flag = True
            break
    if flag:
        ans += 1
print(ans)