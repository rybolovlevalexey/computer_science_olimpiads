# i and i+5
file = open('zadanie_27_B.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
sp1 = sorted(sp)
print(n)
print(sp1[:100])
print(sp1[0], sp1[1], sp1[2], sp1[3])
print(sp.index(sp1[0]), sp.index(sp1[1]), sp.index(sp1[2]), sp.index(sp1[3]))