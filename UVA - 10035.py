while(True):
    try:
        num = list(map(int, input().split()))
        a = num[0]; b = num[1]
        if a == 0 and b == 0:
            break
        carry = 0
        c = 0
        while a > 0 and b > 0:
            if (a % 10 + b % 10 + carry) >= 10:
                c += 1
                carry = 1
                a = a // 10
                b = b // 10
            else:
                carry = 0
                a = a // 10
                b = b // 10
        if c > 0:
            print(c, "carry operations.")
        else:
            print("No carry operation.")
    except EOFError:
        break