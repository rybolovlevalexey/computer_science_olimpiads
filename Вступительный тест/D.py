import sqlite3

file_name = input()
invis = int(input())
criteria = input()

con = sqlite3.connect(file_name)
cur = con.cursor()

places = cur.execute(f'''select id, name from places''')
places_dict = dict()
for elem in places:
    places_dict[elem[0]] = elem[1]
result = cur.execute(
    f'''select place_id, {criteria}, invisibility from demiguisse where invisibility >= {invis}''')
ans_sp = list()
for elem in result:
    ans_sp.append([places_dict[elem[0]], elem[1], elem[2]])
for i in range(len(ans_sp) - 1):
    for j in range(len(ans_sp) - i - 1):
        if ans_sp[j][2] < ans_sp[j + 1][2] or ans_sp[j][2] == ans_sp[j + 1][2] and \
                ans_sp[j][0] > ans_sp[j + 1][0]:
            ans_sp[j], ans_sp[j + 1] = ans_sp[j + 1], ans_sp[j]
for elem in ans_sp:
    print(elem[0], elem[1])
