t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    m = l[0]
    n = l[1]
    q = l[2]
    array = []
    for i in range(m):
        row = list(input())
        array.append(row)
    for s in range(q):
        l = list(map(int, input().split()))
        r = l[0]
        c = l[1]
        square = True
        d = 0
        while square:
            if r - d < 0 or r + d >= m or c - d < 0 or c + d >= n:
                break 
            for i in range(r - d, r + d + 1):
                for j in range(c - d, c + d + 1):
                    if array[i][j] != array[r][c]:
                        square = False
                        break
            if square:
                d += 1
        if s == 0:
            print(m, n, q, end = "\n")
        if d != 1:
            d = d * 2 - 1
        print(d, end = "\n")