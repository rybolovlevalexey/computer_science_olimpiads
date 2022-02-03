cnt_good = 0
j = 1
st = input()
while st != "И будет нам счастье!":
    if cnt_good == 5:
        break
    new_st = st[0:len(st) - j + 1:j + 1]
    new_st = set(list(new_st))
    if len(new_st) >= 7:
        print(st)
        cnt_good += 1
    j += 1
    st = input()
