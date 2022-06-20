from itertools import product, permutations
cnt = 0
sp = ['в', 'з', 'г', 'л', 'я', 'д']

for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                st = i1 + i2 + i3 + i4
                if st.count('з') == 1 or st.count('з') == 2:
                    cnt += 1
print(cnt)

words = list(product(sp, repeat=4))
cnt = 0
for wor in words:
    if ''.join(wor).count('з') == 1 or ''.join(wor).count('з') == 2:
        cnt += 1
print(cnt)

words = permutations(sp)
print(*words)