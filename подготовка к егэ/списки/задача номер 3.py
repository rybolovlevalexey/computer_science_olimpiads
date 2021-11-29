file = open('17_3.txt', 'r')
text = list(map(int, file.read().strip().split('\n')))
ans = 0
sp = list()
for i in range(len(text) - 2):
    first = text[i]
    second = text[i + 1]
    third = text[i + 2]
    if (first + third) / 2 == second:
        ans += 1
        sp.append(first + second + third)
print(ans, max(sp), sp)
