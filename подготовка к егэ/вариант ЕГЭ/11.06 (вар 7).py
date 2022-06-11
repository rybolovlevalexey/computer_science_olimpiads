ans = list()
d1 = 29
while True:
    nechet = d1**4
    if nechet > 50_000_000:
        break
    while True:
        if 45_000_000 <= nechet <= 50_000_000:
            ans.append(nechet)
        if nechet > 50_000_000:
            break
        nechet *= 2
    d1 += 2
print(*sorted(ans), sep='\n')