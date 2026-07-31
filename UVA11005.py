def covert(num, base):
    if num == 0:
        return [0]

    digit = []
    while num > 0:
        digit.append(num % base)
        num //= base

    return digit[::-1]


t = int(input())

for case in range(t):
    cost = []

    # 讀入36個字元成本
    for _ in range(4):
        cost.extend(map(int, input().split()))

    n = int(input())

    print(f"Case {case + 1}:")

    for _ in range(n):
        num = int(input())

        base_cost = []

        # 計算2~36進位的列印成本
        for base in range(2, 37):
            digit = covert(num, base)

            total = 0
            for d in digit:
                total += cost[d]

            base_cost.append(total)

        minn = min(base_cost)

        ans = []
        for i in range(len(base_cost)):
            if base_cost[i] == minn:
                ans.append(i + 2)

        print(f"Cheapest base(s) for number {num}:", *ans)

    if case != t - 1:
        print()