file = open('128003.txt', 'r')
text = file.read().strip().split('\n')
s = 0
t = 0
ans = 0
for elem in text:
    for letter in elem:
        if letter == 'S':
            s += 1
        if letter == 'T':
            t += 1
    if s == t:
        pass