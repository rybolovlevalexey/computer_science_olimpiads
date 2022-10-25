n = int(input())
ans = open('output.txt', 'w')
for i in range(n):
    name = input()
    file = open(name, 'r')
    data = file.readlines()
    if len(data) > 0 and i + 1 != n:
        data[-1] += '\n'
    if len(data) == 0:
        ans.write('\n')
    else:
        ans.write(''.join(data))
ans.close()