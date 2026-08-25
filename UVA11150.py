while True:
    try:
        n = int(input())
        maxx = n
        b = n  # 初始空瓶數

        # 只要空瓶數 >= 3 就可以正常兌換
        while b >= 3:
            new_cola = b // 3
            maxx += new_cola
            b = new_cola + (b % 3)

        # 如果最後剛好剩 2 個空瓶，借 1 個湊滿 3 個換可樂，喝完剛好還 1 個
        if b == 2:
            maxx += 1

        print(maxx)

    except EOFError:
        break