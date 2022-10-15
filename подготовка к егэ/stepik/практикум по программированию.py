file = open('file.txt')
sp = file.readlines()
words = 0
letters = 0
for elem in sp:
    while '  ' in elem:
        elem = elem.replace('  ', ' ')
    for wor in elem.split():
        words += 1
        for let in wor:
            if 97 <= ord(let.lower()) <= 122:
                letters += 1
print('Input file contains:')
print(f'{letters} letters')
print(f'{words} words')
print(f'{len(sp)} lines')