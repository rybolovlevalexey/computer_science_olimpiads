file = open('17_1.txt', 'r')
text = list(map(int, file.read().strip().split('\n')))
ans = 0
sp = list()

for i in range(len(text) - 1):
    first = (text[i])
    second = (text[i + 1])
    if first % 2 == 1 and second % 2 == 1:
        sr = (first + second) // 2
        if sr in text:
            ans += 1
            sp.append(sr)
print(ans, max(sp))
