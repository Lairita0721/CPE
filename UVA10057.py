while True:
    try:
        n = int(input())

        num = []
        for _ in range(n):
            num.append(int(input()))

        num.sort()

        # 左右兩個中位數
        low = num[(n - 1) // 2]
        high = num[n // 2]

        # 有多少個輸入值落在 [low, high]
        c = 0
        for x in num:
            if low <= x <= high:
                c += 1

        # 可以讓總距離最小的整數數量
        m = high - low + 1

        print(low, c, m)

    except EOFError:
        break