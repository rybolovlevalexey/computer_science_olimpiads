st = input()
num = 0
flag = True
for elem in st:
    if elem == '(':
        num += 1
    else:
        num -= 1
    if num < 0:
        flag = False
        break
if num != 0:
    flag = False
if flag:
    print('Good')  # выводится в том случае, если последовательность составлена корректно
else:
    print('Bad')  # выводится в том случае, если последовательность составлена некорректно
