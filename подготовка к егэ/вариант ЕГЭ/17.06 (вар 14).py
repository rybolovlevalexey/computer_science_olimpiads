n = 1
file = open('24_demo (2).txt', 'r')
st = file.read().strip()
ans = list()
for i in range(1, 10000):
    if st.count('Y' * i) >= 1:
        ans.append(i)
print(max(ans))