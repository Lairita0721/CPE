t = int(input())
l = []
for i in range(t):
    a = int(input())
    b = int(input())
    if a % 2 == 0:
        a += 1
    if b % 2 == 0:
        b -= 1
    if a <= b:
        n = (b - a) // 2 + 1
        ans = n * (a + b) // 2
    else:
        ans = 0
    l.append(ans)
for j in range(len(l)):
    index = j + 1
    print(f"Case {index}: {l[j]}", end = "\n")
    