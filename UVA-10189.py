x = 1
while True:
    try:
        l = list(map(int, input().split()))
        n = l[0]
        m = l[1]
        if n == 0 and m == 0:
            break
        array = []
        c = [[0] * m for _ in range(n)]
        for i in range(n):
            array.append(list(input()))
        for i in range(n):
            for j in range(m):
                if array[i][j] == "*":
                    minex = j
                    miney = i 
                    if minex - 1 < 0:
                        left = minex
                    else:
                        left = minex - 1
                    if minex + 1 >= m:
                        right = minex
                    else:
                        right = minex + 1
                    if miney - 1 < 0:
                        hight = miney
                    else:
                        hight = miney - 1
                    if miney + 1 >= n:
                        depth = miney
                    else:
                        depth = miney + 1

                    for r in range(hight, depth + 1):
                        for s in range(left, right + 1):
                            if (r != miney or s != minex) and c[r][s] != '*':
                                c[r][s] += 1
                            else:
                                c[r][s] = '*'
        
                    
        if x != 1:
            print()
        print(f"Field #{x}:")
        for i in range(n):
            ans = ""
            for j in range(m):
                ans += str(c[i][j])
            print(ans)
        x += 1
    except EOFError:
        break