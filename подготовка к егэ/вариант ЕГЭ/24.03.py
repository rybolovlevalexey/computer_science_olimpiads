for num in range(10000, 99999 + 1):
    st1 = int(str(num)[0]) + int(str(num)[2]) + int(str(num)[4])
    st2 = int(str(num)[1]) + int(str(num)[3])
    ans = str(min(st1, st2)) + str(max(st1, st2))
    if ans == '621':
        print(num)
        break
