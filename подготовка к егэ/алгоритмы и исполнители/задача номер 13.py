minimum = -1
for i in range(21):
    for j in range(21):
        for k in range(21):
            if k + j + i != 20:
                continue
            time1 = i * 5
            time2 = j * 7
            time3 = k * 9
            if minimum == -1 or max(time1, time2, time3) < minimum:
                minimum = max(time1, time2, time3)
print(minimum)