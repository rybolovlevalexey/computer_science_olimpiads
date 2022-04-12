sp = [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0]
ind = 10
while sp[ind] == 1:
    ind -= 1
while sp[ind] == 0:
    ind -= 1
ind -= 1
while sp[ind] == 1:
    ind += 1
    sp[ind] = 0
while sp[ind] == 0:
    ind += 1
ind -= 1
sp[ind] = 1
ind -= 1
while sp[ind] == 0:
    ind -= 1
ind -= 1
print(sp)