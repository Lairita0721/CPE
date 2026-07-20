while(True):
    try:
        n = list(map(int, input().split()))
        if len(n) <= 0:
            break
        s = n[0]
        d = n[1]
        l = 0
        r = d
        while l <= r:
            mid = (l + r) // 2
            days = (mid + 1) * (2 * s + mid) / 2
            if days >= d:
                r = mid - 1
            else:
                l = mid + 1

        print(s + l)
    except EOFError:
        break