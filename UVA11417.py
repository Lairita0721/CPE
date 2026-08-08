import math
while (True):
    try:
        n = int(input())
        total = 0
        if n == 0:
            break
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += math.gcd(i, j)
        print(total, end = "\n")
    except EOFError:
        break