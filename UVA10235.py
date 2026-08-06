while(True):
    try:
        prime = True
        emirp = True
        n = int(input())
        root = int(n ** 0.5)
        for i in range(2, root + 1):
            if n % i == 0:
                prime = False
                break
        m = int(str(n)[::-1])
        if n != m:
            root_m = int(m ** 0.5)
            for i in range(2, root_m + 1):
                if m % i == 0:
                    emirp = False
                    break
        else:
            emirp = False
        if prime == False:
            print(n, "is not prime.", end = "\n")
        elif emirp == False:
            print(n, "is prime.", end = "\n")
        else:
            print(n, "is emirp.", end = "\n")
    except EOFError:
        break