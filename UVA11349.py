t = int(input())
symmetric = True
for r in range(t):
    l = list(input().split())
    n = int(l[2])
    array = []
    for i in range(n):
        row = list(map(int, input().split()))
        array.append(row)
    for i in range(n):
        for j in range(n):
            if array[i][j] < 0:
                symmetric = False
            if array[i][j] != array[n - 1 - i][n - 1 -j]:
                symmetric = False
                break
    c = r + 1
    if symmetric == True:
        print(f"Test #{c}: Symmetric.", end = "\n")
    else:
        print(f"Test #{c}: Non-symmetric.", end = "\n")