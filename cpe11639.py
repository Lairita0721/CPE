#11639
n = int(input())
for i in range(n):
    land = [[0] * 100 for _ in range(100)]
    s = 0
    w = 0
    u = 10000
    input_1 = list(map(int, input().split()))
    x1 = input_1[0]
    y1 = input_1[1]
    x2 = input_1[2]
    y2 = input_1[3]
    for j in range(x1, x2):
        for k in range(y1, y2):
            land[j][k] += 1
    input_2 = list(map(int, input().split()))
    x1 = input_2[0]
    y1 = input_2[1]
    x2 = input_2[2]
    y2 = input_2[3]
    for j in range(x1, x2):
        for k in range(y1, y2):
            land[j][k] += 1
    for j in range(100):
        for k in range(100):
            if land[j][k] == 2:
                s += 1
            elif land[j][k] == 1:
                w += 1
    u = u - s - w
    print(f"Night {i + 1}: {s} {w} {u}", end = "\n")