while (True):
    try:
        n = int(input())
        if n == 0:
            break
        sum = 0
        degree = 0
        a = n
        while a > 0:
            sum += a % 10
            a = a // 10
        degree += 1
        if sum % 9 != 0:
            print(n, "is not a multiple of 9.", end = "\n")
        else:
            while sum > 9:
                a = sum
                sum = 0
                while a > 0:
                    sum += a % 10
                    a = a // 10
                degree += 1
            print(f"{n} is a multiple of 9 and has 9-degree {degree}.", end = "\n")
    except EOFError:
        break