n = int(input())
for i in range(n):
    r = 0
    minn = 0
    summ = 0
    l = list(map(int,input().split()))
    r = l[0]
    del l[0]
    l.sort()
    if r % 2 == 0:
        for s in l:
            summ += abs(s - l[(r // 2) - 1])
        minn = summ
        summ = 0
        for s in l:
            summ += abs(s - l[(r // 2)])
        if summ < minn:
            minn = summ
    else:
        for s in l:
            summ += abs(s - l[(r // 2)])
        minn = summ
    print(minn)