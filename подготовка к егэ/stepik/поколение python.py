n = int(input())
t = n * 45
t += 15 * ((n % 2 + 1) % 2)
if n % 2 == 1:
    n -= 1
else:
    n -= 2
t += n // 2 * 20
h = 9 + t // 60
m = t % 60
print(h, m)