file = open('prices.txt')
sp = file.readlines()
su = 0
for elem in sp:
    name, cnt, cost = elem.split('\t')
    su += int(cnt) * int(cost)
print(su)