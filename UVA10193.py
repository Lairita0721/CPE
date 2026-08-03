n = int(input())
for _ in range(n):
    s1 = int(input(), 2)
    s2 = int(input(), 2)
    q = 0
    while s2 > 0:
        r = s1 % s2
        s1 = s2
        s2 = r
    if s1 > 1:
        print(f"Pair #{_ + 1}: All you need is love!", end = "\n")
    else:
        print(f"Pair #{_ + 1}: Love is not all you need!", end = "\n")        