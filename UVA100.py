memo = {1: 1}

def cycle(n):
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        memo[n] = 1 + cycle(n // 2)
    else:
        memo[n] = 1 + cycle(3 * n + 1)

    return memo[n]

while True:
    try:
        a, b = map(int, input().split())

        left = min(a, b)
        right = max(a, b)

        max_cycle = 0

        for i in range(left, right + 1):
            c = cycle(i)
            if c > max_cycle:
                max_cycle = c

        print(a, b, max_cycle)

    except EOFError:
        break