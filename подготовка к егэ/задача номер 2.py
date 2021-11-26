sp = ['к', 'р', 'о', 'т']
answer = 0
for a1 in sp:
    for a2 in sp:
        for a3 in sp:
            for a4 in sp:
                for a5 in sp:
                    for a6 in sp:
                        if list([a1, a2, a3, a4, a5, a6]).count('о') == 1:
                            answer += 1
                            print(a1+a2+a3+a4+a5+a6)
print(answer)