import random
sp = list()
for i in range(int(input())):
    sp.append(input())
friends = sp[::-1]
if len(sp) % 2 == 1:
    friends[len(sp) // 2], friends[-1] = friends[-1], friends[len(sp) // 2]
for i in range(len(sp)):
    print(sp[i], friends[i], sep=' - ')