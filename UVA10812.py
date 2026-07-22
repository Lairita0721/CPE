n = int(input())
ans = []
for i in range(n):
    num = list(map(int, input().split()))
    s = num[0]
    d = num[1]
    if d > s:
        print("impossible", end = "\n")
    else:
        if (s + d) % 2 != 0:
            print("impossible", end = "\n")
        else:
            a = int((s + d) / 2)
            b = s - a
            if a < 0 or b < 0:
                print("impossible", end = "\n")
        
            elif a >= b:
                print(a, b, end = "\n")
            else:
                print(b, a, end = "\n")