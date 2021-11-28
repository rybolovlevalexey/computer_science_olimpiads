file = open('k7a-1.txt', 'r')
text = file.read().strip()
ans = -1
x = 0
for i in range(len(text)):
    elem = text[i]
    if elem in 'ABC':
        x += 1
    else:
        if ans == -1 or ans < x:
            ans = x
        x = 0
print(ans)
print(text)