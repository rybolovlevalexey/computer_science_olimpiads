st = input().split()
letters = dict()
for let in st:
    if let in letters:
        print(f'{let}_{letters[let]}', end=' ')
        letters[let] += 1
    else:
        print(let, end=' ')
        letters[let] = 1