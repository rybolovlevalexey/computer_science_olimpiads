file = open('24-1 (1).txt', 'r')
st = file.read().strip()
letters = ''
answers = list()
for i in range(1, len(st)):
    if letters == '' and st[i - 1] > st[i]:
        letters += st[i] + st[i - 1]
    elif letters != '' and st[i - 1] > st[i]:
        letters += st[i]
    elif letters != '' and st[i - 1] <= st[i]:
        answers.append(letters)
        letters = ''
answers.append(letters)
print(len(max(answers, key=lambda x: len(x))))