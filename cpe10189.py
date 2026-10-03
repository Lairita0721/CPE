#10189
t = 1
while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        mine = [[0] * b for _ in range(a)]
        for i in range(a):
            line = input()
            for j, c in enumerate(line):
                if c == '*':
                    mine[i][j] = '*'
                    if i - 1 >= 0:
                        d = i - 1
                    else:
                        d = i
                    if i + 1 < a:
                        u = i + 1
                    else:
                        u = i
                    if j - 1 >= 0:
                        l = j - 1
                    else:
                        l = j
                    if j + 1 < b:
                        r = j + 1
                    for x in range(d, u + 1):
                        for y in range(l, r + 1):
                            if mine[x][y] != '*':
                                mine[x][y] += 1
        if t != 1:
            print()
        print(f"Field #{t}:", end = "\n")
        t += 1
        for i in range(a):
            for j in range(b):
                print(mine[i][j], end='')
            print()
                     
    except EOFError:
        break