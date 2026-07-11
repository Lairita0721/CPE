while(True):
    try:
        num = int(input())
        if num == 0:
            break
        fx = 0
        while num >= 10:
            a = num
            while a > 0:
                fx += a % 10
                a = a // 10
            num = fx
            fx = 0
        print(num, end = "\n")
    except EOFError:
        break