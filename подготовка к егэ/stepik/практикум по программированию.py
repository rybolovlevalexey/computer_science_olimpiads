file = open('nums.txt')
sp = file.readlines()
su = 0
for line in sp:
    line = line.strip()
    num = ''
    for x in line:
        if x.isdigit():
            num += x
        else:
            if num != '':
                su += int(num)
            num = ''
    if num != '':
        su += int(num)
print(su)