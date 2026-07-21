t = int(input())
l = []
for i in range(t):
    a = int(input())
    b = int(input())
    n = (b - a) // 2 + 1
    ans = n * (a + b) // 2
    l.append(ans)
for j in range(len(l)):
    index = j + 1
    print(f"Case {index}: {l[j]}", end = "\n")
    