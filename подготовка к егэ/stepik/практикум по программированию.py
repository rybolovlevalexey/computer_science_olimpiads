import random

file = open('data.txt', 'w')
sp = list()
for i in range(10**8):
    num = random.randint(1, 10**6)
    file.write(str(num) + '\n')
file.close()
