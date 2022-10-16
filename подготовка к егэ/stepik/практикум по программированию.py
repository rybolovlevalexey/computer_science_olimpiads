flag = True
name = input()
file = open(name)
sp = file.read().strip().split('\n')
for i in range(0, len(sp)):
    if i == 0 and sp[i][:3] == 'def':
        print(sp[i].split()[1][:sp[i].split()[1].index('(')])
        flag = False
        continue
    if len(sp[i].strip()) >= 3 and sp[i].strip()[:3] == 'def':
        if len(sp[i - 1]) == 0 or sp[i - 1].strip()[0] != '#':
            print(sp[i].split()[1][:sp[i].split()[1].index('(')])
            flag = False
if flag:
    print('Best Programming Team')