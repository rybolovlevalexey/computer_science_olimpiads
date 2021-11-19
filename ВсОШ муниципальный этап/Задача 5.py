n, m, c = map(int, input().split())  # кол-во площадок, кол-во экспедиций, топливо на проезд 1км
ports = dict()  # расстояние до площадки: затраты топлива
for _ in range(n):
    a, b = map(int, input().split())
    ports[a] = b
for m1 in range(m):
    dist = int(input())  # цель экспедиции
    answer = 0
    for key, value in ports.items():
        rashod = value
        dist1 = abs(dist - key)
        rashod += dist1 * c
        if answer == 0 or rashod < answer:
            answer = rashod
    print(answer)
