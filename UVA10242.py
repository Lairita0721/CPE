while (True):
    try:
        l = list(map(float, input().split()))
        if not l:
            continue
        x1 = l[0]
        y1 = l[1]
        x2 = l[2]
        y2 = l[3]
        x3 = l[4]
        y3 = l[5]
        x4 = l[6]
        y4 = l[7]
        
        if x1 == x3 and y1 == y3:
            b1 = x1
            b2 = y1
            a1 = x2
            a2 = y2
            c1 = x4
            c2 = y4
        elif x1 == x4 and y1 == y4:
            b1 = x1
            b2 = y1
            a1 = x3
            a2 = y3
            c1 = x2
            c2 = y2
        elif x2 == x3 and y2 == y3:
            b1 = x2
            b2 = y2
            a1 = x1
            a2 = y1
            c1 = x4
            c2 = y4
        else:
            b1 = x2
            b2 = y2
            a1 = x3
            a2 = y3
            c1 = x1
            c2 = y1
        
        ans1 = a1 + c1 - b1
        ans2 = a2 + c2 - b2
        print(f"{ans1:.3f} {ans2:.3f}", end = "\n")

    except EOFError:
        break