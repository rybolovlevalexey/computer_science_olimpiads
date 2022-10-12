n = int(input())
ddeyst = {'execute':'X', 'write':'W', 'read':'R'}
files = dict()
for i in range(n):
    name, *fich = input().split()
    files[name] = fich
print(files)
for j in range(int(input())):
    deyst, name = input().split()
    if name in files and ddeyst[deyst] in files[name]:
        print('OK')
    else:
        print('Access denied')