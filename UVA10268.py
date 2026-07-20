while(True):
    try:
        x = int(input())
        a = list(map(int, input().split()))
        n = len(a) - 1
        summ = 0
        for i in range(n):
            summ += a[i] * (n - i) * x ** (n - i - 1)
        print(summ, end = "\n")
    except EOFError:
        break