for _ in range(20):
    while True:
        try:
            l = list(map(int, input().split()))
            n = l[0]
            m = l[1]
            num = {}
            if n == 0 and m == 0:
                print(n, m)
                break
            for i in range(n):
                a = int(input())
                if a > 0:
                    num[a] = a % m
                elif a < 0:
                    num[a] = abs(a) % m * -1
            print(n, m, end = "\n")    
            for i in sorted(num, key = lambda x:(num[x], 0 if x % 2 else 1, -x if x % 2 else x)):
                print(i, end = "\n")
          
        except EOFError:
            break