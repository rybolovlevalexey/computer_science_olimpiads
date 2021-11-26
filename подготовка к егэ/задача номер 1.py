sp = ['з', 'д', 'а', 'н', 'и', 'е']
glas = ['а', 'и', 'е']
sogl = ['з', 'д', 'н']
answer = 0
for a1 in sp:
    for a2 in sp:
        for a3 in sp:
            for a4 in sp:
                for a5 in sp:
                    for a6 in sp:
                        if len(set(list([a1, a2, a3, a4, a5, a6]))) != 6:
                            continue
                        if (a1 in glas and a2 in glas) or (a3 in glas and a2 in glas) or\
                            (a3 in glas and a4 in glas) or (a4 in glas and a5 in glas) or \
                                (a5 in glas and a6 in glas) or (a1 in sogl and a2 in sogl) or\
                                (a3 in sogl and a2 in sogl) or\
                            (a3 in sogl and a4 in sogl) or (a4 in sogl and a5 in sogl) or \
                                (a5 in sogl and a6 in sogl):
                            continue
                        answer += 1
                        print(a1+a2+a3+a4+a5+a6)
print(answer)