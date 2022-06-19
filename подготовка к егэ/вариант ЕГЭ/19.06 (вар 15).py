file = open('zadanie24_2 (3).txt', 'r')
st = file.read().strip()
ans = list()
for i in range(1, 1000):
    if st.count('L' * i) > 0:
        ans.append(i)
print(max(ans))