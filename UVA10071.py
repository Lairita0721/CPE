while(True):
    try:
        num = list(map(int, input().split()))
        v = num[0]
        t = num[1]
        s = 2 * v * t
        print(s, end = "\n")
    except EOFError:
        break