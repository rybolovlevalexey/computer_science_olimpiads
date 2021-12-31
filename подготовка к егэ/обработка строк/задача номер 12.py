file = open('24-153.txt', 'r')
st = file.read().strip()
all_dliny = list()
indexes = list()
for i in range(len(st)):
    if st[i] == 'D':
        indexes.append(i)
spisok = list()
for i in range(1, len(indexes)):
    spisok.append(indexes[i] - indexes[i - 1] + 1)
print(min(filter(lambda x: x != 2, spisok)))