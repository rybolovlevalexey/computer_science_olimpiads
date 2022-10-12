st = input()
shifr = dict()
for elem in st:
    if elem in shifr:
        shifr[elem] += 1
    else:
        shifr[elem] = 1
n = int(input())
letters = dict()
for i in range(n):
    let, cnt = input().split(': ')
    cnt = int(cnt)
    for key, value in shifr.items():
        if value == cnt:
            letters[key] = let
for elem in st:
    print(letters[elem], end='')