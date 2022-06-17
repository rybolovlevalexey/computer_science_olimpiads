ansd = 0
ans = None
for num in range(568023, 569230+1):
    sp = set()
    sp.add(1)
    sp.add(num)
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            sp.add(d)
            sp.add(num // d)
    if ans is None or len(sp) > ansd:
        ans = num
        ansd = len(sp)
    if len(sp) == 144:
        print(sp)
print(ansd, ans)