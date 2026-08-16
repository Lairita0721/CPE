t = int(input())
for _ in range(t):
    length = int(input())
    order = list(map(int, input().split()))
    c = 0
    for i in range(length):
        for j in range(i + 1, length):
            if order[i] > order[j]:
                order[i], order[j] = order[j], order[i]

                c += 1
    print(f"Optimal train swapping takes {c} swaps.")