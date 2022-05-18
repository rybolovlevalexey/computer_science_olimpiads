cnt = 1
ans = ''
sp = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    st = i1 + i2 + i3 + i4 + i5
                    if cnt == 12769:
                        ans = st
                        print(ans)
                    cnt += 1
print(ans)