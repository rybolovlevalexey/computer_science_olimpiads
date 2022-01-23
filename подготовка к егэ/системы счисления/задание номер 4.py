num = 6 * 343**1156 - 5 * 49**1147 + 4 * 7**1153 - 875
st = []
while num > 0:
    st.append(num % 7)
    num //= 7
print(sum(st))
