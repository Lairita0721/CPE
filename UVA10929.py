while(True):
    try:
        a = input()
        if a == "0":
            break
        even = 0
        odd = 0
        for i in range(len(a)):
            if i % 2 == 0:
                even += int(a[i])
            else:
                odd += int(a[i])
        if abs(even - odd) % 11 == 0:
            print(a, "is a multiple of 11.")
        else:
            print(a, "is not a multiple of 11.")
    except EOFError:
        break