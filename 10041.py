#10041
t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    r = n[0]
    del n[0]
    total = 0
    t1 = 0
    t2 = 0
    n.sort()
    if len(n) % 2 == 0:
        median1 = n[len(n) // 2 - 1]
        median2 = n[len(n) // 2]
        for j in n:
            t1 += abs(median1 - j)
            t2 += abs(median2 - j)
        total = min(t1, t2)
    else:
        median = n[len(n) // 2]
        for j in n:
            total += abs(median - j)
    print(total, end = "\n")