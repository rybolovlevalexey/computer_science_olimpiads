cnt = 1
ans = 0
sp = sorted(['с', 'т', 'е', 'п', 'у', 'х', 'а'])
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                st = i1 + i2 + i3 + i4
                if cnt > 1000 and i1 != i2 and i2 != i3 and i3 != i4:
                    ans += 1
                cnt += 1
print(ans)