from datetime import timedelta
file = open('logfile.txt', encoding='UTF-8')
output = open('output.txt', 'w', encoding='UTF-8')
for line in file.readlines():
    name, start, finish = line.strip().split(', ')
    t_start = timedelta(hours=int(start.split(':')[0]), minutes=int(start.split(':')[1]))
    t_finish = timedelta(hours=int(finish.split(':')[0]), minutes=int(finish.split(':')[1]))
    delta = t_finish - t_start
    if delta >= timedelta(hours=1):
        output.write(name + '\n')
output.close()