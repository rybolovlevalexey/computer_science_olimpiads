dic = {'1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO',
       '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': ' '}
letters = ''
for key, value in dic.items():
    letters += key
    letters += value
st = input().upper()
ans = ''
print(letters)
for let in st:
    if let not in letters:
        continue
    if let in dic.keys():
        ans += let
    else:
        n = 0
        for key, value in dic.items():
            if let not in value:
                continue
            for elem in value:
                n += 1
                if elem == let:
                    ans += key * n
                    break
print(ans)