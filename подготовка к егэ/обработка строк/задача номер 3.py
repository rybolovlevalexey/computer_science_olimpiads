file = open('k7b-4.txt', 'r')
text = file.read().strip()
ans = -1
x = 0
dick = {0: 'E', 1: 'B', 2: 'C', 3: 'F'}
letter_now = 0
for i in range(len(text)):
    elem = text[i]
    letter = dick[letter_now]
    if elem == letter:
        x += 1
        letter_now += 1
        if letter_now == 4:
            letter_now = 0
    else:
        if ans == -1 or ans < x:
            ans = x
        x = 0
        letter_now = 0
print(ans)