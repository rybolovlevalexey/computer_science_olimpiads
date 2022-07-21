def beegeek(a, b):
    ans = ''
    for i in range(a, b + 1):
        if i % 21 == 0:
            ans += 'BeeGeek '
        elif i % 3 == 0:
            ans += 'Bee '
        elif i % 7 == 0:
            ans += 'Geek '
        else:
            ans += (str(i) + ' ')
    return ans.strip()
