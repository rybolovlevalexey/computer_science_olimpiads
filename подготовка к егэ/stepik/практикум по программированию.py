let = {10: 'qz', 8: 'jx', 5: 'k', 4: 'fhvwy', 3: 'bcmp', 2: 'dg'}
letters = ''
for value in let.values():
    letters += value
st = input().lower()
su = 0
for i in st:
    if i not in letters:
        su += 1
    else:
        for key, value in let.items():
            if i in value:
                su += key
print(su)