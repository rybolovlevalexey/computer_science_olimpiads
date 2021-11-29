file = open('17_1 (1).txt', 'r')
text = list(map(int, file.read().strip().split('\n')))
ans = 0
sp = list()
for i in range(len(text) - 1):
    first = text[i]
    second = text[i + 1]
    if first % 5 == 0 or second % 5 == 0:
        if (first + second) % 10 != 0 and (first + second) in text:
            ans += 1
            sp.append(first + second)
print(ans, max(sp))
