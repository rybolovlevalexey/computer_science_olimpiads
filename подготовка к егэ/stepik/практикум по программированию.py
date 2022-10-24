sp_x = list()
sp_y = list()
sp_z = list()
for i in range(3):
    dots = list(map(float, input().split()))
    if i == 0:
        sp_x = dots
    elif i == 1:
        sp_y = dots
    else:
        sp_z = dots
print(all(list(d <= 4 for d in map(lambda x: x[0]**2 + x[1]**2 + x[2]**2, zip(sp_x, sp_y, sp_z)))))