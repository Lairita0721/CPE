def value(ch):
    if ch.isdigit():
        return int(ch)
    elif 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') + 10
    else:
        return ord(ch) - ord('a') + 36


while True:
    try:
        num = input().strip()

        digit_sum = 0
        max_digit = 0

        for ch in num:
            if ch == '+' or ch == '-':
                continue

            v = value(ch)
            digit_sum += v
            max_digit = max(max_digit, v)

        start = max(max_digit + 1, 2)

        found = False
        for base in range(start, 63):
            if digit_sum % (base - 1) == 0:
                print(base)
                found = True
                break

        if not found:
            print("such number is impossible!")

    except EOFError:
        break