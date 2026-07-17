while(True):
    try:
        jolly = True
        n = 0
        l = []
        num = list(map(int, input().split()))
        n = num[0]
        seq = num[1:]
        for i in range(1, n):
            l.append(i)
            
        for i in range(n - 1):
            a = abs(seq[i] - seq[i + 1])
            if a not in l:
                jolly = False
                print("f")
                break
            else:
                print(a)
                l.remove(a)
        if jolly == True:
            print("Jolly", end = "\n")
        else:
            print("Not jolly", end = "\n")
    except EOFError:
        break