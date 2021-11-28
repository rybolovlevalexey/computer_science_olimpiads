file = open('k7a-4.txt', 'r')
text = file.read().strip()
max_lenght = -1
lenght = 0
for i in range(len(text)):
    elem = text[i]
    if elem == 'D':
        if max_lenght == -1 or lenght > max_lenght:
            max_lenght = lenght
        lenght = 0
    else:
        lenght += 1
print(max_lenght)