c = 1
while(True):
    try:
        line = input()
        if line =="":
            continue
        n = int(line)
        ##if len(n) == 0:
            ##break
        summ = set()
        b2 = True
        num = list(map(int, input().split()))
        for i in range(n):
            if num[i] <= 0:
                b2 = False

        for i in range(n-1):
            if num[i] >= num[i+1]:
                b2 = False
        for i in range(n):
            for j in range(i , n):
                if b2 == False:
                    break
                a = num[i] + num[j]
                if a not in summ:
                    summ.add(a)
                else:
                    b2 = False
                    break
        if b2 == True:
            print(f"Case #{c}: It is a B2-Sequence.", end = "\n")
            ##print(sum)
        else:
            print(f"Case #{c}: It is not a B2-Sequence.", end = "\n")
            ##print(sum)
        c += 1
        print()
    except EOFError:
        break