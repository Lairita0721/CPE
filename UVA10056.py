s = int(input())
for _ in range(s):
    num = list(input().split())
    n = int(num[0])
    p = float(num[1])
    i = int(num[2])
    if p == 0:
        print("0.0000")
    else:
        probability = (p * (1 - p) ** (i - 1)) / (1 - (1 - p) ** n)
        print(f"{probability:.4f}")