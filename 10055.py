#10055
while True:
    try:
        n = list(map(int, input().split()))
        d = abs(n[1] - n[0])
        print(d, end = "\n")
    except EOFError:
        break