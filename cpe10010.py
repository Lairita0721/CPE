#cpe10010
t = int(input())
blank = input()
for i in range(t):
    m, n = map(int, input().split())
    text = []
    search = []
    location = []
    for j in range(m):
        text.append(input().lower())
    k = int(input())
    for j in range(k):
        search.append(input().lower())
    possible = False
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for j in range(k):
        for r in range(m):
            for s in range(n):
                if text[r][s] == search[j][0]:
                    for di, dj in direction:
                        possible = True
                        for l in range(len(search[j])):
                            ni = r + di * l
                            nj = s + dj * l
                            if ni < 0 or ni >= m or nj < 0 or nj >= n or text[ni][nj] != search[j][l]:
                                possible = False
                                break
                        if possible:
                            location.append((r + 1, s + 1))
                            break
            if possible:
                break
    if possible:
        for loc in location:
            print(loc[0], loc[1])
    else:
        print("NO")