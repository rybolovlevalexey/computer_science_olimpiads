file = open('24_demo.txt', 'r')
st = file.read().strip()
n = 1
while True:
    if st.count('XYZ' * n) >= 1:
        ans = n
    else:
        break
    n += 1

print(st.count('XYZ' * 4 + 'X'))