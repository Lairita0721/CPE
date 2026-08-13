def step(x, y):
    return (x + y) * (x + y + 1) // 2 + x

t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    s = step(x1, y1)
    d = step(x2, y2)
    ans = d - s
    print(f"Case {i + 1}: {ans}")