file = open('24 (7).txt', 'r')
sp = file.read().strip().split('XZZY')
print(len(max(sp, key=lambda x: len(x))) + 6)