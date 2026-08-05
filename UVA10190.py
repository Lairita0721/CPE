while (True):
    try:
        l = list(map(int, input().split()))
        n = l[0]
        m = l[1]
        a = [n]
        boring = False
        if n < 2 or m < 2:
            print("Boring!")
            continue
        while n != 1:
            if n % m == 0:
                n = n // m 
                a.append(n)
            else:
                print("Boring!", end = "\n")
                boring = True
                break
        if boring == False:
            print(" ".join(map(str, a)), end = "\n")
    except EOFError:
        break