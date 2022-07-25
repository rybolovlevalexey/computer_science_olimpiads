t = int(input())
while t > 3600 * 24:
    t -= 3600 * 24
h = t // 3600
t = t - h * 3600
s = t % 60
m = t // 60
s = t - m * 60
s = '0' * (2 - len(str(s))) + str(s)
m = '0' * (2 - len(str(m))) + str(m)
print(f'{h}:{m}:{s}')
