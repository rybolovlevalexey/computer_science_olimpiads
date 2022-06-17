n = 1
file = open('24_demo (2).txt', 'r')
st = file.read().strip()
while st.count('Y' * (n + 1)) >= 1:
    n += 1
print(n)
print(st.count('Y' * 11))