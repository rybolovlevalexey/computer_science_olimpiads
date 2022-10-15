file = open('numbers.txt')
sp = file.readlines()
for line in sp:
    line = line.strip()
    while '  ' in line:
        line = line.replace('  ', ' ')
    print(sum(map(int, line.split())))