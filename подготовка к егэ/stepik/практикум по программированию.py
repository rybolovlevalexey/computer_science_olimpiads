sp = ['1', '2', '2', '3', '3']
ans = set()
for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    if i1 + i2 + i3 + i4 + i5 == 10:
                        st = sp[i1] + sp[i2] + sp[i3] + sp[i4] + sp[i5]
                        ans.add(st)
                        print(st)
print(len(ans))
