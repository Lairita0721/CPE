while(True):
    try:
        num = list(map(int, input().split()))
        s = num[0]
        o = num[1]
        total = 0
        total = o - s
        print(total)
    except EOFError:
        break