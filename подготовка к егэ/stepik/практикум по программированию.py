file = open('class_scores.txt', 'r')
file1 = open('new_scores.txt', 'w')
for line in file.readlines():
    fam, score = line.strip().split()
    score = (int(score) + 5)
    if score > 100:
        score = 100
    file1.write(str(fam) + ' ' + str(score) + '\n')
file.close()
file1.close()